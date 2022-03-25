from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def contacts():
    return render_template("signup.html")

app.run(host="localhost", port=5000, debug=True)