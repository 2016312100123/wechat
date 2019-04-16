#！/usr/bin/python
#-*- coding:UTF-8 -*-
import json
import requests
import os

url = 'http://192.168.37.132:8002/service_class/test_Converg'
headers = {'content-type':'application/json'}
data = {'sentence':"我已经还了",'flag':'pay','project_id':'2'}
r = requests.post(url,data=json.dumps(data),headers=headers)
print(r)
print(r.text)