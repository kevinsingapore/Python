#!/usr/bin/python2
#-*- coding:UTF-8 -*-

import urllib2
import re

url = urllib2.urlopen("http://myip.ipip.net")

text = url.read()

ip = re.search('\d+.\d+.\d+.\d+',text).group()

print(text)

print(ip)
