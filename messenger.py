# -*- coding: utf-8 -*-
import requests
apiurl = '你的地址'
apiheaders = {'U-ApiKey': '你的key'}
code="动态码"
response = requests.get(apiurl, params={"media_id":'gh_3fc78df4c9d2',"auth_code":code, "scene":1,"device_no":1,"location":'jia'})
json = response.json()
print(json)
   
