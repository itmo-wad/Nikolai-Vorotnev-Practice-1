from http import client
from re import L
from flask import g, redirect, request
from wsgiref.util import request_uri
from flask import Flask, render_template
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/practice1"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/auth', methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = mongo.db.users.find_one({
            "username" : username
        })
        if password == (user['password']):
            return render_template("secret.html")
        else:
            return 'Access denied'

        return 'Input: ' + username + '; ' + password
    else:
        return render_template("auth.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        mongo.db.users.insert_one({
            "username" : username, 
            "password" : password
        })
        return "You was successfully registered!"
    else:
        return render_template("signup.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        return render_template('upload.html')
    else:
        if 'image' not in request.files:
            flash('No file')
            return redirect(request.url)

        file = request.files['image']

        if not file or file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        app.config['UPLOAD_FOLDER'] = 'Upload'

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect(request.url)
app.run(host="localhost", port=5000, debug=True)