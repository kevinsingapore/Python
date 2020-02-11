#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import os

#创建多层目录
os.makedirs(r'./a/b/c')

#删除多层目录
os.removedirs('./a/b/c')

#获取当前目录文件列表
list = os.listdir('.')

print(list)
