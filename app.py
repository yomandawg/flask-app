from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/<string:name>")
def index(name=None):
    foo = {
        "title": "Flask Example",
        "bar": "Hello, World!",
        "name": name
    }
    return render_template("index.html", **foo)

if __name__ == "__main__":
    app.run(debug = True)