from flask_restful import Resource
from flask import render_template
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)


class DefaultRouter(Resource):
  def get(self):
    return render_template("index.html")

  def get(self, name):
    foo = {
      "title": "Flask Example",
      "bar": "Hello, World!",
      "name": name
    }
    return render_template("index.html", **foo)


class DBRouter(Resource):
  def get(self):
    online_users = client.db.users.find()
    print(dict(online_users))
    return json.dumps(dict(online_users))
