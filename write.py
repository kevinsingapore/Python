#!/usr/bin/python3
#-*- coding: UTF-8 -*-

f = open("google.html",mode="a",encoding="utf-8")
f.write("yum -y install vim")
f.flush()
f.close()
c = open("google.html",mode="r",encoding="utf-8")
content = c.read()
print(content)
c.close()
