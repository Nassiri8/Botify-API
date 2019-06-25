import pymysql
import hashlib
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flaskext.mysql import MySQL

class traitement:
    def fields(self, list):
        if list:
            return True
        return False
    
    def query(self, list):
        i = 1
        element = '{}'
        if self.fields(list) == True:
            nb = len(list)
            while i <= nb:
                query = 'SELECT'+element+' FROM towns'
                i+=1
        return query


class dsl(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fields', type=list, location='json')
        parser.add_argument('filters', type=dict, location='json')
        args = parser.parse_args()
        t = traitement()
        return t.query(args)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = 'SELECT {}, {} FROM towns'.format(args['fields'][0], args['fields'][1])
        cursor.execute(query)
        rows = cursor.fetchall()
        return jsonify(rows)