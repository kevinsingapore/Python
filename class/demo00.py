#!/usr/bin/python3
#-*- coding:UTF-8 -*-

class Potato:
  def __init__(self,name):
      self.name = name
  def kick(self):
      print('我叫%s,噢~谁踢我?' % self.name)

kevin = Potato('kevin')

print(kevin.kick())
