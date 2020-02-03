#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import requests

r = requests.get('https://api.github.com/user',auth=('user','Sa123***'))

status = r.status_code

encoding = r.encoding

text = r.text

json = r.json()

print(status)
print(encoding)
print(text)
print(json)
