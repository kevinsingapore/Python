#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import os

os.makedirs(r'./a/b/c')

dirs = os.walk('.')

for i in dirs:
  print(i)
