# encoding=utf-8

from flask import Flask,render_template,request

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/api",methods=["GET"])
def api():
    return "api"



if __name__ == '__main__':
    app.run(
        port = 7777,
        debug = True
    )
