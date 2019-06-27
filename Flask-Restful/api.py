import pymysql
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flaskext.mysql import MySQL
import sys
sys.path.insert(0, './controller')
from town import *
from aggs import *
from dsl import *

api = Api(app)

class Home(Resource):
    def get(self):
        return {'message':'Welcome Friends'}

api.add_resource(Home, '/')

#Routes for towns and parameter
api.add_resource(towns, '/towns')
api.add_resource(TownByName, '/town/<string:name>')
api.add_resource(deleteTown, '/town/delete/<string:name>')
api.add_resource(townByRegion, '/town/region/<string:region>')
api.add_resource(townWithMore, '/town/<int:population>')

#Routes for aggs
api.add_resource(aggs, '/aggs')

#Route for DSL
api.add_resource(dsl, '/query')

if __name__ == '__main__':
    app.run()
