#!/usr/bin/python3
#-*- coding:UTF-8 -*-

stu = ['id','name','sex','age','course']

#append()方法支持追加1个参数
stu.append(['english','math'])

print(stu)
print(type(stu))

#extend()方法支持以列表方式追加参数
stu.extend(['5','8',['sky','kevin'],'women'])

print(stu)
