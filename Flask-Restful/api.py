import pymysql
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flaskext.mysql import MySQL
import sys
sys.path.insert(0, './controller')
from town import *

api = Api(app)

class Home(Resource):
    def get(self):
        return {'message':'Welcome Friends'}

#Routes for home
api.add_resource(Home, '/')
api.add_resource(towns, '/towns')
api.add_resource(TownByName, '/town/<string:name>')
api.add_resource(deleteTown, '/town/delete/<string:name>')
api.add_resource(townByRegion, '/town/region/<string:region>')
api.add_resource(townWithMore, '/town/<int:population>')

if __name__ == '__main__':
    app.run()
