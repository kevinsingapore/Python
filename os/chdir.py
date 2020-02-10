#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import os

#改变工作目录
old_path = os.chdir('/Users/kevin/')
new_path = os.getcwd()
print(new_path)
