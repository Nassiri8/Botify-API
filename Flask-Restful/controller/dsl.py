import pymysql
import hashlib
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flaskext.mysql import MySQL

class traitement:
    #Check exist
    def fields(self, list):
        if list:
            return True
        return False
    
    #Basic Query "SELECT 'element' FROM 'table'"
    def querySimple(self, list):
        if self.fields(list['fields'])== True and list['fields'] and not None:
            i=0
            queryParams = ""
            while i < len(list['fields']):
                queryParams += list['fields'][i] + ","
                i+=1
            queryParams = queryParams[:-1]
            query= 'SELECT ' + queryParams + ' FROM towns'
        return query
    
    #Query with only field and value
    def queryFilter(self, list):
        if self.fields(list['filters']) == True and list['filters'] is not None or not list['filters']:
            i= 0
            queryParams = ""
            while i < len(list['fields']):
                queryParams += list['fields'][i] + ","
                i+=1
            queryParams = queryParams[:-1]
            if list["filters"]["field"] and list["filters"]["value"]:
                query= 'SELECT '+queryParams+' FROM towns WHERE '+list["filters"]["field"]+"= "+str(list["filters"]["value"])
                return query
        return False
    
    #Query with predicate in JSON
    def queryPredicate(self, list):
        predicate = {"gt": ">", "lt": "<", "equal":"=", "contains": "LIKE"}
        if self.fields(list['filters']) == True and list['filters'] is not None or not list['filters']:
            i= 0
            queryParams = ""
            while i < len(list['fields']):
                queryParams += list['fields'][i] + ","
                i+=1
            queryParams = queryParams[:-1]
            if list["filters"]["field"] and list["filters"]["value"] and list['filters']['predicate']:
                query=""
                if list['filters']['predicate'] == "gt":
                    list['filters']['predicate'] = predicate['gt']
                    query= 'SELECT '+queryParams+' FROM towns WHERE '+list["filters"]["field"]+" "+list['filters']['predicate']+" "+str(list["filters"]["value"])
                if list['filters']['predicate'] == "lt":
                    list['filters']['predicate'] = predicate['lt']
                    query= 'SELECT '+queryParams+' FROM towns WHERE '+list["filters"]["field"]+" "+list['filters']['predicate']+" "+str(list["filters"]["value"])
                if list['filters']['predicate'] == "equal":
                    list['filters']['predicate'] = predicate['equal']
                    query= 'SELECT '+queryParams+' FROM towns WHERE '+list["filters"]["field"]+" "+list['filters']['predicate']+" "+str(list["filters"]["value"])
                if list['filters']['predicate'] == "contains":
                    list['filters']['predicate'] = predicate['contains']
                    query= 'SELECT '+queryParams+' FROM towns WHERE '+list["filters"]["field"]+" "+list['filters']['predicate']+" "+str(list["filters"]["value"])
                return query
        return False

    #return list of string for the AND 
    def checkListAnd(self, list):
        predicate = {"gt": ">", "lt": "<", "equal":"=", "contains": "LIKE"}
        query=[]
        condi = ""
        i = 0
        if list['filters']['and']:
            while i < len(list['filters']['and']):
                if list['filters']['and'][i]['predicate'] == "gt":
                    list['filters']['and'][i]['predicate'] = predicate['gt']
                    condi = list['filters']['and'][i]['field'] + " "+ list['filters']['and'][i]['predicate']+" "+str(list['filters']['and'][i]['value'])+" AND "
                    query.append(condi)
                    i+=1 
                if list['filters']['and'][i]['predicate'] == "lt":
                    list['filters']['and'][i]['predicate'] = predicate['lt']
                    condi = list['filters']['and'][i]['field'] + " "+ list['filters']['and'][i]['predicate']+" "+str(list['filters']['and'][i]['value'])+" AND "
                    query.append(condi)
                    i+=1
                if list['filters']['and'][i]['predicate'] == "equal":
                    list['filters']['and'][i]['predicate'] = predicate['equal']
                    condi = list['filters']['and'][i]['field'] + " "+ list['filters']['and'][i]['predicate']+" "+str(list['filters']['and'][i]['value'])+" AND "
                    query.append(condi)
                    i+=1
                if list['filters']['and'][i]['predicate'] == "contains":
                    list['filters']['and'][i]['predicate'] = predicate['contains']
                    condi = list['filters']['and'][i]['field'] + " "+ list['filters']['and'][i]['predicate']+" "+str(list['filters']['and'][i]['value'])+"OR "
                    query.append(condi)
                    i+=1
            return query

    #return list with string for the OR
    def checkListOr(self, list):  
        predicate = {"gt": ">", "lt": "<", "equal":"=", "contains": "LIKE"}
        query = []
        condi = ""
        i = 0
        if list['filters']['or']:
            while i < len(list['filters']['or']):
                if list['filters']['or'][i]['predicate'] == "gt":
                    list['filters']['or'][i]['predicate'] = predicate['gt']
                    condi = list['filters']['or'][i]['field'] + " "+ list['filters']['or'][i]['predicate']+" "+str(list['filters']['or'][i]['value'])+"OR "
                    query.append(condi)
                    i+=1
                if list['filters']['or'][i]['predicate'] == "lt":
                    list['filters']['or'][i]['predicate'] = predicate['lt']
                    condi = list['filters']['or'][i]['field'] + " "+ list['filters']['or'][i]['predicate']+" "+str(list['filters']['or'][i]['value'])+"OR "
                    query.append(condi)
                    i+=1
                if list['filters']['or'][i]['predicate'] == "equal":
                    list['filters']['and'][i]['predicate'] = predicate['equal']
                    condi = list['filters']['or'][i]['field'] + " "+ list['filters']['or'][i]['predicate']+" "+str(list['filters']['or'][i]['value']) +"OR "
                    query.append(condi)
                    i+=1
                if list['filters']['or'][i]['predicate'] == "contains":
                    list['filters']['or'][i]['predicate'] = predicate['contains']
                    condi = list['filters']['or'][i]['field'] + " "+ list['filters']['or'][i]['predicate']+" "+str(list['filters']['or'][i]['value'])+"OR "
                    query.append(condi)
                    i+=1
            return query
    
    #return string about condition "Pop = ... AND/OR ..."            
    def createCondition(self, list):
        if list['filters']['and']:
            condi = self.checkListAnd(list)
            str1 = ''.join(str(e) for e in condi)
            str1 = str1[:-4]
            return str1
        if list['filters']['or']:
            condi = self.checkListOr(list)
            str1 = ''.join(str(e) for e in condi)
            str1 = str1[:-3]
            return str1

    #Query for AND/OR
    def queryAndOr(self, list):
        query = ""
        if self.fields(list['filters']) == True and list['filters'] is not None or not list['filters']:
            i= 0
            queryParams = ""
            while i < len(list['fields']):
                queryParams += list['fields'][i] + ","
                i+=1
            queryParams = queryParams[:-1]
            condition = self.createCondition(list)
            if condition:
                query = "SELECT "+ queryParams+" FROM towns WHERE "+condition
            return query

    #Traitement du lancement query ERROR
    def queryChoose(self, list):
        query = ""
        if list['fields'] and list['filters'] is None:
            query = self.querySimple(list)
        if list["fields"] and list["filters"] and list["filters"]["field"] and list["filters"]["value"]:
            query = self.queryFilter(list)
        if list["filters"]["field"] and list["filters"]["value"] and list["fields"] and list['filters']['predicate']:
            query= self.queryPredicate(list)
        return query

""""if list["fields"] and list["filters"] and list["filters"]["and"] or list["filters"]["or"]:
            query = self.queryAndOr(list)"""
        
class dsl(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fields', type=list, location='json')
        parser.add_argument('filters', type=dict, location='json')
        args = parser.parse_args()
        t = traitement()
        return t.queryAndOr(args)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        if args['fields'] is not None and args['filters'] is not None:
            rq = t.queryChoose(args)
            cursor.execute(rq)
            rows = cursor.fetchall()
            return jsonify(rows)
        return jsonify({'about':'bad Json format'})