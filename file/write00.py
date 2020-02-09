#!/usr/bin/python3
#-*- coding:UTF-8 -*-

f = open('hello.txt','w')
f.write('hello,')
f.write('kevin!')
f.close()

w = open('hello.txt','r')
print(w.read())
