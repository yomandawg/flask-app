from flask import Flask
from flask import render_template
from flask_restful import Api
from handlers.handler import DBRouter

#testing git-flow1

app = Flask(__name__)


@app.route('/')
@app.route('/<string:name>')
def get(name="hello"):
    foo = {
        "title": "Flask Example",
        "bar": "Hello, World!",
        "name": name
    }
    return render_template("index.html", **foo)


api = Api(app)
api.add_resource(DBRouter, '/db')

if __name__ == "__main__":
    app.run(debug=True)
