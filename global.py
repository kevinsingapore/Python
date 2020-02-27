#!/usr/bin/python3
#-*- coding:UTF-8 -*-


num = 88

#------------------------------
def myFun():
  num = 10  
  print(num)
  return num

myFun()

print(num)
print('-----------------------')

#-------------------------------
def myNewFun():
  global num
  num = 10
  print(num)
  return num

myNewFun()

print(num)



