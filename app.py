from http import client
from re import L
from flask import g, request
from wsgiref.util import request_uri
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/practice1"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = mongo.db.users.find_one({})
        if password == (user['password']):
            return 'Success'
        else:
            return 'Access denied'

        return 'Input: ' + username + '; ' + password
    else:
        # print (mongo.db.find())
        return render_template("signup.html")
        

app.run(host="localhost", port=5000, debug=True)