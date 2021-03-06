from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__)

    api = Api(app)

    from .handlers.handler import DBRouter, ShoppingRouter, \
        TrendRouter, TestHandler

    api.add_resource(DBRouter, '/api/db')
    api.add_resource(ShoppingRouter, '/api/shopping')
    api.add_resource(TrendRouter, '/api/trend/<string:search>')
    api.add_resource(TestHandler, '/api/test')

    return app
