from flask import Flask, render_template
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


@app.route("/")
@app.route("/<string:name>")
def index(name="Index"):
    foo = {
        "title": "Flask Example",
        "bar": "Hello, World!",
        "name": name
    }
    return render_template("index.html", **foo)

@app.route("/db")
def home_page():
    online_users = mongo.db.users.find()
    print(dict(online_users))
    return json.dumps(dict(online_users))

if __name__ == "__main__":
    app.run(debug=True)
