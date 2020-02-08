#!/usr/bin/python3
#-*- coding:UTF-8 -*-

def discount(price,rate):
    final_price = price * rate
    return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discount(old_price,rate)

print('打折后的价格是:%.2f' % new_price)
