from bson import ObjectId

class JsonUtil():
  def toJson(self, data):
    for i in data:
      if i == '_id':
        data[i] = str(data[i])
    return data
