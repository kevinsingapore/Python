#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import os

#新建文件夹kevin
os.mkdir('kevin')
print(os.listdir('.'))

#删除文件夹kevin
os.rmdir('kevin')
print(os.listdir('.'))



