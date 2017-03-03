# coding:utf-8

import json

__author__ = 'hzliyong'

data = {"id":"1016423","pvid":"","abtest":"你好"}

in_json = json.dumps(data, ensure_ascii = True)
print(in_json)
pythonJson = json.loads(in_json)
print(type(pythonJson))
print(pythonJson['id'])
print(pythonJson['abtest'])
