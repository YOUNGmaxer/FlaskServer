import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
  def default(self, o):
    # 如果是 ObjectId 对象，就转化为字符串
    if isinstance(o, ObjectId):
      return str(o)
    return json.JSONEncoder.default(self, o)
