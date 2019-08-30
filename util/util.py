# encoding=utf-8

import json
import os

root = "config/guide1.json"

def read_guide():
    if os.path.exists(root):
        with open(root, 'r',encoding="utf-8") as f:
            load_dict = json.loads(f.read())
            return load_dict

def write_guide(load_dict):
    with open("config/guide.json", "w",encoding="utf-8") as f:
        json.dump(load_dict, f, ensure_ascii=False,indent=2)
		

