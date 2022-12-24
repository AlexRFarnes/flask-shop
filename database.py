from peewee import *
from decouple import config


db = MySQLDatabase(
    database=config("database"),
    user=config("user"),
    password=config("password"),
    port=config("port"),
    host=config("host")
)

class User(Model):
    email=""
    password=""
    created_at=""