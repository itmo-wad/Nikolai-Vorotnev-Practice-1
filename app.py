from http import client
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/practice1"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def contacts():
    return render_template("signup.html")

app.run(host="localhost", port=5000, debug=True)