# encoding=utf-8
# @Time    : 2017/12/26 17:32
# @Author  : Zuo Ran
# @File    : Util.py
import os


class Util(object):
    # 获取当前项目路径
    @staticmethod
    def get_project_path():
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        return path
