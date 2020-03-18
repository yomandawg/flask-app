from flask import Flask
from flask_restful import Api, Resource
from .naver import naver
import json

app = Flask(__name__)
api = Api(app)

class NaverApi(Resource):
    def get(self):
        return naver()

api.add_resource(NaverApi, '/')


if __name__ == "__main__":
    app.run(debug=True)