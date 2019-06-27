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
                    #return query
                if list['filters']['predicate'] == "lt":
                    list['filters']['predicate'] = predicate['lt']
                    query= 'SELECT '+queryParams+' FROM towns WHERE '+list["filters"]["field"]+" "+list['filters']['predicate']+" "+str(list["filters"]["value"])
                    #return query
                if list['filters']['predicate'] == "equal":
                    list['filters']['predicate'] = predicate['equal']
                    query= 'SELECT '+queryParams+' FROM towns WHERE '+list["filters"]["field"]+" "+list['filters']['predicate']+" "+str(list["filters"]["value"])
                    #return query
                if list['filters']['predicate'] == "contains":
                    list['filters']['predicate'] = predicate['contains']
                    query= 'SELECT '+queryParams+' FROM towns WHERE '+list["filters"]["field"]+" "+list['filters']['predicate']+" "+str(list["filters"]["value"])
                    print(query)
                    #return query
                return query
        return False

    #Traitement du lancement query ERROR
    def queryChoose(self, list):
        query = ""
        if list["filters"]["field"] and list["filters"]["value"] and list["fields"] and list['filters']['predicate']:
            query= self.queryPredicate(list)
        if list["filters"]["field"] and list["filters"]["value"] and list["fields"] and list["filters"]:
            query = self.queryFilter(list)
        if list['fields']:
            query = self.querySimple(list)
        else:
            return "bad JSON Format"
        return query
        
class dsl(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fields', type=list, location='json')
        parser.add_argument('filters', type=dict, location='json')
        args = parser.parse_args()
        t = traitement()
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        rq = t.queryChoose(args)
        cursor.execute(rq)
        rows = cursor.fetchall()
        return jsonify(rows)