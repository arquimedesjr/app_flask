from flask import render_template
from app import app

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
@app.route("/")
def login():
    return render_template('base.html')
