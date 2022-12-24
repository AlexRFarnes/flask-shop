from flask import Flask
from flask import render_template
from flask import request
# from markupsafe import escape

from database import User

app = Flask(__name__)


# @app.route("/<name>")
# def index(name):
#     return f"<h1>Hello, {escape(name)}!</h1>"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email and password:
            user = User.create(email=email, password=password) # INSERT
            print(user.id)


    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
