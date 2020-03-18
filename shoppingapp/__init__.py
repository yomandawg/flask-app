from flask import Flask
from flask_restful import Api


def create_app():
    app = Api(Flask(__name__))

    from .handlers.handler import DBRouter, ShoppingRouter

    app.add_resource(DBRouter, '/api/db')
    app.add_resource(ShoppingRouter, '/api/shopping')

    setattr(app, "testing", True)

    return app