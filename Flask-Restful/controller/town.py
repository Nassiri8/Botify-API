import pymysql
import hashlib
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flaskext.mysql import MySQL

class bears(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM bears')
        rows = cursor.fetchall()
        resp = jsonify(rows)
        if not rows:
            return jsonify({'about':'no bears found'})
        resp.status_code = 200
        return resp

class deleteBear(Resource):
    def delete(self, id):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('DELETE FROM bears WHERE id = %s', id)
        conn.commit()
        return jsonify({'about':'bears delete'})

class addBear(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='name')
        parser.add_argument('device', type=str, required=True, help='device')
        args = parser.parse_args()
        name = args['name']
        device = args['device']
        if name and device:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id FROM tracker WHERE device = %s", device)
            rows = cursor.fetchall()
            if not rows:
                return jsonify({'about':'cannot add bears error'})
            sqlQuery = 'INSERT INTO bears(name , tracker_id) VALUES ("{}", {})'.format(name, rows[0]["id"])
            cursor.execute(sqlQuery)
            conn.commit()
            return jsonify({'created':'bears with tracker on add'})
            

class bearByName(Resource):
    def get(self, name):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM bears WHERE name = %s', name)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        if not rows:
            return jsonify({'about':'no bears found'})
        resp.status_code = 200
        return resp

class lastPositionBear(Resource):
    def get(self, name):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT bears.name, tracker.lat, tracker.lng, tracker.country, tracker.time, tracker.date FROM bears INNER JOIN tracker ON bears.tracker_id = tracker.id WHERE bears.name = %s ORDER BY tracker.time DESC, tracker.date DESC LIMIT 1", name)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        if not rows:
            return jsonify({'about':'no bears found'})
        resp.status_code = 200
        return resp

