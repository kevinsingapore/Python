#!/usr/bin/python3
#-*- coding:UTF-8 -*-

from subprocess import run

pwd = run('pwd').stdout

print(pwd)
