from peewee import *
from decouple import config
import datetime


db = MySQLDatabase(
    database=config("database"),
    user=config("user"),
    password=config("password"),
    port=config("port"),
    host=config("host")
)

class User(Model):
    email = TextField()
    password = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)