#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import os

g = os.walk("g:/py/",topdown=True)

for root, dirs, files in g:
    for dirs_name in dirs:
        print("打印目录列表:")
        print(os.path.join(root,dirs_name))
        print("打印所有文件列表(涵子目录及文件):")
    for files_name in files:
        print(os.path.join(root,files_name))


