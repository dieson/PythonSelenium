# encoding=utf-8
# @Time    : 2018/7/27 15:37
# @Author  : Zuo Ran
# @File    : test.py
from Utils.Utils import Utils
import unittest

# 加载测试集
Utils.assert_str_contains_str("PPTP是连接效率最高的隧道协议。","PPTP是连接效率最高的隧道协议。在没有特定连接性能要求时，推荐选用安全性更好的其它协议。"
                              )
