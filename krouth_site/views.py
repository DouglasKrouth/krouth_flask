from flask import render_template

def index():
    return render_template("index.html")

def hello():
    return 'Hello, World'
