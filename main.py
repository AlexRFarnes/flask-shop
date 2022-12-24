from flask import Flask
from flask import render_template
# from markupsafe import escape

from database import db

app = Flask(__name__)


# @app.route("/<name>")
# def index(name):
#     return f"<h1>Hello, {escape(name)}!</h1>"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
