from flask import Flask

from pymongo import MongoClient


def init(app: Flask):

    credentials = (app.config.get('MONGO_USER'), app.config.get('MONGO_PASS'))
    global client
    client = MongoClient(
        "mongodb://{credentials}{host}:{port}/{options}".format(
            credentials=":".join(credentials) if any(credentials) else "",
            host=app.config.get('MONGO_HOST'),
            port=app.config.get('MONGO_PORT'),
            options="?"+app.config.get('MONGO_OPTS')))

    if database_name := app.config.get('MONGO_DBNAME'):
        global db
        db = client[f"{database_name}"]
