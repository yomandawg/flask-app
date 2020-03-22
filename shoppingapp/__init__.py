from flask import Flask
from flask_restful import Api

from flask import render_template

import json


def create_app():
    app = Flask(__name__)

    api = Api(app)

    from .handlers.handler import DBRouter, ShoppingRouter, TestHandler, RayHandler

    api.add_resource(DBRouter, '/api/db')
    api.add_resource(ShoppingRouter, '/api/shopping')
    api.add_resource(TestHandler, '/api/test')
    api.add_resource(RayHandler, '/ray')

    return app