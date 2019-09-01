# encoding=utf-8

from flask import Flask,render_template,request,jsonify
from util import util
import threading
import json

app = Flask(__name__)

@app.route('/')
def guide_page():
    datas = util.read_guide()
    return render_template("index.html",datas = datas,page="blocks/guide.html")

@app.route('/script')
def script_page():
    datas = util.get_script_files()
    return render_template("index.html",datas = datas,page="blocks/shortcut.html")

@app.route("/add",methods=["POST"])
def add():
    data = json.loads(str(request.data,"utf-8"))
    datas = util.read_guide()
    if datas is not None:
        exitst = False
        for d in datas:
            if d["fieldName"] == data["fieldName"]:
                d["items"].append({
                    "name":data["name"],
                    "url":data["url"],
                    "logo":data["logo"]
                })
                exitst = True
                break
        if not exitst:
            datas.append({
                    "fieldName": data["fieldName"],
                    "items": [{
                            "name": data["name"],
                            "url": data["url"],
                            "logo": data["logo"]
                        }]
                })
    else:
        datas = [{
                    "fieldName": data["fieldName"],
                    "items": [{
                            "name": data["name"],
                            "url": data["url"],
                            "logo": data["logo"]
                        }]
                }]

    util.write_guide(util.root,datas)
    util.update_guide(None)
    return "OK"

@app.route("/add-script",methods=["POST"])
def add_script():
    data = json.loads(str(request.data,"utf-8"))
    util.add_script_file(data["name"],data["content"])
    return "OK"

@app.route("/exec-script",methods=["POST"])
def exec_script():
    data = json.loads(str(request.data,"utf-8"))
    output = util.exec_script(data["script"],data["param"])
    return jsonify({"output":output})



if __name__ == '__main__':
    refreshThread = threading.Thread(target=util.listen_file_modify)
    refreshThread.setDaemon(True)
    refreshThread.start()
    app.run(
        port = 7777,
        debug = True
    )
