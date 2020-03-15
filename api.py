from flask import Flask
from flask_restful import Api
from handlers.handler import DefaultRouter, DBRouter

app = Flask(__name__)
api = Api(app)
api.add_resource(DefaultRouter, '/', '/<string:name>')
api.add_resource(DBRouter, '/db')

if __name__ == "__main__":
    app.run(debug=True)
