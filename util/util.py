# encoding=utf-8

import json

def read_guide():
    with open("config/guide.json", 'r',encoding="utf-8") as f:
        load_dict = json.loads(f.read())
        print(load_dict)

def write_guide(load_dict):
    with open("config/guide.json", "w",encoding="utf-8") as f:
        json.dump(load_dict, f, ensure_ascii=False,indent=2)

