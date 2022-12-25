from flask import Flask
from flask import session # DICT
from flask import render_template
from flask import request
# from markupsafe import escape

from flask_bcrypt import Bcrypt

from database import User

app = Flask(__name__)
app.secret_key = "&ald$skcmjd54545edf&e154ee!115#e4c1aa35gH%"
bcrypt = Bcrypt(app)


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
            pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")
            user = User.create(email=email, password=pw_hash) # INSERT
            session['user'] = user.id

    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
