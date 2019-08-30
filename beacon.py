# encoding=utf-8

from flask import Flask,render_template,request
from util import util

app = Flask(__name__)

@app.route('/')
def index():
    # v = {"orderItem":"name","orderWay":"asc","fields":[{"fieldName":"内网","items":[{"id":1,"name":"百度","url":"https://www.baidu.com","logo":"https://www.baidu.com/img/bd_logo1.png"},{"id":1,"name":"百度","url":"https://www.baidu.com","logo":"https://www.baidu.com/img/bd_logo1.png"}]},{"filedName":"外网","items":[{"id":1,"name":"百度","url":"https://www.baidu.com","logo":"https://www.baidu.com/img/bd_logo1.png"},{"id":1,"name":"百度","url":"https://www.baidu.com","logo":"https://www.baidu.com/img/bd_logo1.png"}]}]}
    util.read_guide()
    return render_template("index.html")

@app.route("/api",methods=["GET"])
def api():
    return "api"

if __name__ == '__main__':
    app.run(
        port = 7777,
        debug = True
    )
