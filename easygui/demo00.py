#!/usr/bin/python3
#-*- coding:UTF-8 -*

import easygui as eg
import sys

while 1:
  eg.msgbox('嗨，欢迎进入第一个界面小游戏^_^!')
  msg = '请问你想到鱼C工作室学到什么知识呢?'
  title = '小游戏互动'
  choices = ['谈恋爱','编程','游戏','琴棋书画']

  choice = eg.choicebox(msg,title,choices)

  eg.msgbox('你的选择是:' + str(choice),'结果')
  
  msg = '你希望重新开始游戏吗?'
  title = '请选择'

  if eg.ccbox(msg,title):
     pass
  else:
     sys.exit(0)
