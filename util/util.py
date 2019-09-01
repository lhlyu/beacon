# encoding=utf-8

import json
import os
import threading
import time
import sys

lock = threading.Lock()

#
GUIDE = None

root = "config/guide.json"
script_dir = "scripts"

def read_guide():
    global GUIDE
    if GUIDE is not None:
        return GUIDE
    if os.path.exists(root):
        with open(root, 'r',encoding="utf-8") as f:
            load_dict = json.loads(f.read())
            update_guide(load_dict)
            return load_dict
    return None

def write_guide(filePath,load_dict):
    with open(filePath, "w",encoding="utf-8") as f:
        json.dump(load_dict, f, ensure_ascii=False,indent=2)
        update_guide(None)
		

def update_guide(guide):
    global GUIDE
    lock.acquire()
    GUIDE = guide
    lock.release()

def listen_file_modify():
    global GUIDE
    print("监听配置文件...")
    lastStat = os.stat(root)
    lastModifyTime = lastStat.st_mtime
    while True:
        newStat = os.stat(root)
        modifyTime = newStat.st_mtime
        if lastModifyTime != modifyTime :
            h = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(modifyTime))
            print("配置文件有所改动，重新加载...",h)
            lastModifyTime = modifyTime
            # 备份
            lock.acquire()
            guide = GUIDE
            lock.release()
            write_guide(root+".bak",guide)
            update_guide(None)
        time.sleep(10)

def get_script_files():
    if not os.path.exists(script_dir):
        os.mkdir(script_dir)
    try:
        fileList = os.listdir(script_dir)
        datas = []
        for file in fileList:
            data = {
                "name":os.path.splitext(file)[0],
                "script":file
            }
            datas.append(data)
        print(datas)
        return datas
    except Exception as e:
        print(e)
        return None

def add_script_file(name,content):
    root = os.path.join(script_dir,name + ".py")
    with open(root,"w",encoding="utf-8") as f:
        f.write(content)

def exec_script(script,param):
    output = "没有结果返回"
    print(sys.getdefaultencoding())
    print(f"输入:{script} {param}")
    try:
        cmd = f"python {script_dir}/{script} {param}"
        print("----->",cmd)
        output = os.popen(cmd).read()
    except Exception as e:
        print(e)
    print(f"输出:{output}")
    return output