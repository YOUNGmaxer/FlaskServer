from flask_pymongo import PyMongo
from flask import jsonify
from api.app import app
from flask_restful import Resource, Api
from api.util.jsonEncode import JSONEncoder
from api.util.jsonUtil import JsonUtil
import json

mongo = PyMongo(app)
api = Api(app)

class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}

class City(Resource):
  def get(self):
    data = mongo.db.城市名单.find()
    data = JsonUtil().toJson(data[0])
    return data

api.add_resource(HelloWorld, '/hello')
api.add_resource(City, '/city')
