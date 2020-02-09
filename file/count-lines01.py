#!/usr/bin/python3
#-*- coding:UTF-8 -*-
import sys
import os
from subprocess import run

for index,line in enumerate(open('keywords.txt','r')):
  with open('count.txt','a') as f:
    print((index,line),file=f)

file = open('count.txt','r')
print(file.read())

fi = open('count.txt','r')
lines = fi.readlines()
for line in lines:
  if '武汉' in line:
    if '中国' in line:
      print(line)

rm_stdout = os.remove('count.txt')
print(rm_stdout)

#f = open('count.txt','r')
#lines = f.readlines()
#for line in lines:
#  if '武汉' in line:
#    if '中国' in line:
#      print(line)





