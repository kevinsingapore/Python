#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import os

f = os.walk('.')

for root, dirs, files in f:
  for dirs_name in dirs:
    print(os.path.join(root,dirs_name))
  for files_name in files:
    print(os.path.join(root,files_name))
