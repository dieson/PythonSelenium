# encoding=utf-8
# @Time    : 2018/5/30 11:04
# @Author  : Zuo Ran
# @File    : test.py
import os
from Utils.LoggerUtils import LoggerUtils
from Utils.Utils import Utils

def test(a,b):
    print a + b
    a += 1
    print a +b

test(1, 2)