#!/usr/bin/python3
#-*- coding:UTF-8 -*-

try:
  int(10.12)
  sum = 1 + 1
  f = open('我是一个不存在的文件.txt','r')
  print(f.read())
  f.closed

except (OSError,TypeError) as reason:
  print('出错啦!' + str(reason))
