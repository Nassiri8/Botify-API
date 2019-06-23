import pymysql
import hashlib
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flaskext.mysql import MySQL

class aggs(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM towns')
        rows = cursor.fetchall()
        resp = jsonify(rows)
        if not rows:
            return jsonify({'about':'no towns found'})
        resp.status_code = 200
        return resp