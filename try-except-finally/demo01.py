#!/usr/bin/python3
#-*- coding:UTF-8 -*-

try:
  sum = 1 + 1.5
  data = int(sum)
  f = open('demo.py','r')
  print(f.read())

except OSError as reason:
  print('出错啦T_T\n 原因是:' + str(reason))

finally:
  f.close()
