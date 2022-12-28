from flask import Flask
from flask import session # DICT
from flask import render_template
from flask import request
from flask import redirect
# from markupsafe import escape

from decouple import config

from flask_bcrypt import Bcrypt

from database import User
from database import Product

app = Flask(__name__)
app.secret_key = config('FLASK_SECRET_KEY')
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
            session['user_id'] = user.id # ID del usuario en la base de datos

            return redirect("/products")

    return render_template("register.html")


@app.route("/products")
def products():
    user_id = User.get(session["user_id"])

    # products = Product.select().where(Product.user_id == user_id)
    products = user_id.products

    return render_template("products/index.html", products=products)


@app.route("/products/create", methods=["GET", "POST"])
def products_create():
    if request.method == "POST":
        name = request.form.get("name")
        price = float(request.form.get("price"))*100

        if name and price:
            user_id = User.get(session["user_id"]) # SELECT * FROM users WHERE id = <id>
            Product.create(name=name, price=price, user_id=user_id)

            return redirect("/products")

    return render_template("products/create.html")


@app.route("/products/<id>/update", methods=["GET", "POST"])
def products_update(id):
    product = Product.get(id)

    if request.method == "POST":
        name = request.form.get("name")
        price = float(request.form.get("price"))

        if name and price:
            # user_id = User.get(session["user_id"]) # SELECT * FROM users WHERE id = <id>
            product.name = name
            product.price = price
            product.save()

            return redirect("/products")


    return render_template("products/update.html", product=product)

# delete route

if __name__ == "__main__":
    app.run(debug=True)
