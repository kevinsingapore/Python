#!/usr/bin/python3
#-*- coding:UTF-8 -*-

num = range(1,1001,1)

f = open('num.txt','w')
for i in num:
  print(i,file=f)

f.close()
