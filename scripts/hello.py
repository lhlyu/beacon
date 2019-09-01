# encoding=utf-8
import os,sys

if __name__ == '__main__':
    params = sys.argv[1:]
    s = ",".join(params)
    print(f"hello {s}")