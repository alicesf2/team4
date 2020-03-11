import pymongo
import os

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = pymongo.MongoClient(
    "mongodb+srv://alicesf2:<password>@team4-y2pw0.mongodb.net/test?retryWrites=true&w=majority")
db = pymongo.database.Database(mongo, 'team4')
users = pymongo.collection.Collection(db, 'users')


# a simple page that says hello
@app.route('/', methods=['GET'])
def hello():
    output = []
    for u in users.find():
        output.append({'username': u['username']})
    return jsonify({'result': output})


@app.route('/goodbye')
def goodbye():
    return "Goodbye, World!"
