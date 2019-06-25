import pymysql
import hashlib
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flaskext.mysql import MySQL

class traitement:
    def queryChoose(self, list):
        if list['fields'] and list['filters']:
            return True
        return False

    def fields(self, list):
        if list:
            return True
        return False
    
    def querySimple(self, list):
        if self.fields(list['fields'])== True:
            i=0
            queryParams = ""
            while i < len(list['fields']):
                queryParams += list['fields'][i] + ","
                i+=1
            queryParams = queryParams[:-1]
            query= 'SELECT ' + queryParams + ' FROM towns'
        return query
    
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

class dsl(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fields', type=list, location='json')
        parser.add_argument('filters', type=dict, location='json')
        args = parser.parse_args()
        t = traitement()
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(t.queryFilter(args))
        rows = cursor.fetchall()
        return jsonify(rows)