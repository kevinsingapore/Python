#!/usr/bin/python2
#-*- coding:UTF-8 -*-

def exchangeRate(dollar):
  """
  功能:汇率转换:美元->人民币
  汇率:6.54
  日期:2018-06-05
  """
  print dollar * 6.54

if __name__ == '__main__':
  exchangeRate(10)

print(exchangeRate.__doc__)
  
help(exchangeRate)


