#!/usr/bin/python3
#-*- coding:UTF-8 -*-

f = open('seek00.txt','w')
f.write('0123456789987654321')
f.seek(5)
f.write('hello')
f.close()

f = open('seek00.txt','r')
print(f.read())
f.close()

