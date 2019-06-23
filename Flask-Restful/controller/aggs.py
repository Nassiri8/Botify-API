import pymysql
import hashlib
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flaskext.mysql import MySQL

class aggs(Resource):
    def checkExist(a):
        if not a:
            a = None
            return a
        return a
    def get(self):
        parser.add_argument('district', type=int, help='code district')
        parser.add_argument('depart', type=str, help='code department')
        district= checkExist(args['district'])
        depart= checkExist(args['depart'])
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT COUNT(Town_Name), MAX(Population), MIN(Population), AVG(Average_Age) FROM `towns` WHERE Code_District = %s OR Code_Department = %s', district, depart)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        if not rows:
            return jsonify({'about':'no data found'})
        resp.status_code = 200
        return resp