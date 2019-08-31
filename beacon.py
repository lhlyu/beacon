# encoding=utf-8

from flask import Flask,render_template,request
from util import util
import threading
import json

app = Flask(__name__)

@app.route('/')
def index():
    datas = util.read_guide()
    return render_template("index.html",datas = datas)

@app.route("/add",methods=["POST"])
def api():
    print(json.loads(str(request.data,"utf-8")))
    data = json.loads(str(request.data,"utf-8"))
    datas = util.read_guide()
    for d in datas:
        if d["fieldName"] == data["fieldName"]:
            d["items"].append({
                "name":data["name"],
                "url":data["url"],
                "logo":data["logo"]
            })
            break
    util.write_guide(util.root,datas)
    util.update_guide(None)
    return "OK"

if __name__ == '__main__':
    refreshThread = threading.Thread(target=util.listen_file_modify)
    refreshThread.setDaemon(True)
    refreshThread.start()
    app.run(
        port = 7777,
        debug = True
    )
