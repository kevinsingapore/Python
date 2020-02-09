#!/usr/bin/python3
#-*- coding:UTF-8 -*-

f = open('sample01.txt','w')
f.write('武汉加油！中国加油！')
f.close()

file = open('sample01.txt','r')
#print(file.read(4))
print(file.read())
file.close()
