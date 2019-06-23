import pymysql
import hashlib
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flaskext.mysql import MySQL

class towns(Resource):
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

class deleteTown(Resource):
    def delete(self, name):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('DELETE FROM towns WHERE Town_Name = %s', name)
        conn.commit()
        return jsonify({'about':'town delete'})

class TownByName(Resource):
    def get(self, name):
        name = '%'+name
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM towns WHERE Town_Name LIKE %s', name)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        if not rows:
            return jsonify({'about':'no town found'})
        resp.status_code = 200
        return resp

class townByRegion(Resource):
    def get(self, region):
        region = '%'+region
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM towns WHERE Region_Name LIKE %s', region)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        if not rows:
            return jsonify({'about':'no town found'})
        resp.status_code = 200
        return resp

class townWithMore(Resource):
    def get(self, population):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM `towns` WHERE Population > %s', population)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        if not rows:
            return jsonify({'about':'no town found with more than ' + population})
        resp.status_code = 200
        return resp