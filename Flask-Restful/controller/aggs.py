import pymysql
import hashlib
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flaskext.mysql import MySQL

def convertJson(rows):
    i = 0
    array = []
    while i < len(rows):
         dict ={'towns number': rows[i]['COUNT(Town_Name)'], 'average age': rows[i]["AVG(Average_Age)"], 'max population': rows[i]["MAX(Population)"], 'min population': rows[i]["MIN(Population)"]}
         array.append(dict)
         i+=1
    return array

def checkExist(a):
    if not a:
        a = 'null'
        return a
    return a

class aggs(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('district', type=int, help='code district')
        parser.add_argument('depart', type=str, help='code department')
        args = parser.parse_args()
        district= checkExist(args['district'])
        depart= checkExist(args['depart'])
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = 'SELECT COUNT(Town_Name), MAX(Population), MIN(Population), AVG(Average_Age) FROM towns WHERE Code_District = {} OR Code_Department = {}'.format(district, depart)
        cursor.execute(query)
        rows = cursor.fetchall()
        resp = jsonify(convertJson(rows))
        if not rows:
            return jsonify({'about':'no data found'})
        resp.status_code = 200
        return resp