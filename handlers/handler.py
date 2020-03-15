from flask_restful import Resource
from flask import render_template
import json




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
    online_users = mongo.db.users.find()
    print(dict(online_users))
    return json.dumps(dict(online_users))
