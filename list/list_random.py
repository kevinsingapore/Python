#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import random

kevin = ['fuqiang',29,'man','shenzhen']

print(kevin)

#random()方法随机从列表中取一个元素，适用抽奖功能
prize = random.choice(kevin)

print(prize)

