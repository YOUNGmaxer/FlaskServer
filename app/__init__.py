from flask import Flask

app = Flask(__name__)
# 指定数据库 sights
app.config['MONGO_URI'] = 'mongodb://106.13.70.140:27017/sights'

from api.app import routes
from api.app import api
