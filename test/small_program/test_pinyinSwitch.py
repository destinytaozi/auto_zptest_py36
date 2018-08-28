# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_02
   Description :
   Author :       Destiny
   date：          2018/8/28 11:23
-------------------------------------------------
   Change Activity:
                   2018/8/28 11:23
-------------------------------------------------
"""
__author__ = 'Destiny'

from tkinter import Tk, Text, Button, END, N, GROOVE

root = Tk()
root.geometry('1000x430+600+340')
root.title('[字转拼音]陶子')
hztext = Text(root, width=60, height=25, font='微软雅黑,18')
hztext.grid(row=0, column=0)
from pypinyin import pinyin
Button(root, text='\n\n\n转\n换\n\n\n\n', font='微软雅黑,18', relief=GROOVE,
       command=lambda: pytext.delete('1.0',END) or pytext.insert('1.0', pinyin(hztext.get('1.0', END), heteronym=True)[
                                                                        0:-1])).grid(row=0, column=1, sticky=N)
pytext = Text(root, width=60, height=25, font='微软雅黑,18')
pytext.grid(row=0, column=2)
root.mainloop()
