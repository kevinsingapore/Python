#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import os

#罗列所在目录文件名
files = os.listdir('.')
dirs = os.listdir('..')
path = os.listdir('/Users/kevin/')

print(files)
print(dirs)
print(path)
