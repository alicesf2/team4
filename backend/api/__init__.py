import os

from flask import Flask
from flask_pymongo import PyMongo
from flask import render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://alicesf2:Q9p0y$*hN15I@team4-y2pw0.mongodb.net/test?retryWrites=true&w=majority"
    mongo = PyMongo(app)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/goodbye')
    def goodbye():
        return "Goodbye, World!"

    @app.route('/users')
    def get_users():
        users = mongo.db.users.find({})
        response = render_template("index.html", users=users)
        print(response)
        return response

    return app
