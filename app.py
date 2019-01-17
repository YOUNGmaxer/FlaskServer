from flask import Flask, g, jsonify
import pymongo
import json
from bson import json_util

__all__ = ['app']
app = Flask(__name__)

MONGO_HOST = '106.13.70.140'
MONGO_PORT = 27017
MONGO_DB = 'sights'

def get_mongo():
  if not hasattr(g, 'mongo'):
    g.client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
    g.db = g.client[MONGO_DB]
  return g.db

@app.route('/')
def index():
  return '<h2>Welcome to MongoDB System</h2>'

@app.route('/<string:collection>/find')
def find(collection):
  db = get_mongo()
  data = db[collection].find()
  
  return jsonify(json_util.dumps(data[0]))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)
