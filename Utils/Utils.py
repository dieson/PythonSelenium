# encoding=utf-8
# @Time    : 2017/12/26 17:32
# @Author  : Zuo Ran
# @File    : Utils.py
import os


class Utils(object):
    # 获取当前项目路径
    @staticmethod
    def get_project_path():
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        return path

    @staticmethod
    def get_locator_type(locator):
        if "XPATH" in locator:
            return "XPATH"
        elif "ID" in locator:
            return "ID"
        elif "CLASS" in locator:
            return "CLASS"
        elif "TAGNAME" in locator:
            return "TAGNAME"
        elif "LINKTEXT" in locator:
            return "LINKTEXT"
        elif "NAME" in locator:
            return "NAME"
        elif "CSS" in locator:
            return "CSS"
        else:
            print "[Fail] Unable get locator type"
            return locator

    @staticmethod
    def get_locator_str(locator):
        if "XPATH" in locator:
            return locator.replace("XPATH:", "")
        elif "ID" in locator:
            return locator.replace("ID:", "")
        elif "CLASS" in locator:
            return locator.replace("CLASS:", "")
        elif "TAGNAME" in locator:
            return locator.replace("TAGNAME:", "")
        elif "LINKTEXT" in locator:
            return locator.replace("LINKTEXT:", "")
        elif "NAME" in locator:
            return locator.replace("NAME:", "")
        elif "CSS" in locator:
            return locator.replace("CSS:", "")
        else:
            print "[Fail] Unable get locator string"
            return locator
