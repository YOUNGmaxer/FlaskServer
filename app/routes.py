from api.app import app
from flask import render_template
from flask_pymongo import PyMongo
from flask import jsonify

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
  user = {'username': 'yzm'}
  return render_template('index.html', title='Crawl Project', user=user)

@app.route('/<string:collection>/find', methods=['GET'])
def find(collection):
  data = mongo.db[collection].find()
  print(type(data), data[0])
  return 'right'

@app.route('/test', methods=['GET'])
def test():
  data = { 'ret': 'test' }
  return jsonify(data)
