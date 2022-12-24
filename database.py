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

db.create_tables([User])
