# encoding=utf-8

import json
import os
import threading
import time

lock = threading.Lock()

#
GUIDE = None

root = "config/guide.json"

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

