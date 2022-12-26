from peewee import *
from decouple import config
import datetime


db = MySQLDatabase(
    database=config("database"),
    user=config("user"),
    password=config("password"),
    port=int(config("port")),
    host=config("host")
)


class User(Model):
    email = TextField()
    password = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = "users"


class Product(Model):
    name = TextField()
    price = IntegerField()
    user_id = ForeignKeyField(User, backref='products')
    created_at = DateTimeField(default=datetime.datetime.now)

    @property
    def format_price(self):
        return format(self.price/100, '.2f')

    class Meta:
        database = db
        db_table = "products"



db.create_tables([User, Product])
