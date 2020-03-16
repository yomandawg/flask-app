from flask_restful import Resource
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)

class DBRouter(Resource):
  def get(self):
    online_users = client.db.users.find()
    print(dict(online_users))
    return json.dumps(dict(online_users))
