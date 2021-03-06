# encoding=utf-8
# @Time    : 2017/12/26 17:32
# @Author  : Zuo Ran
# @File    : Utils.py
import os
import configparser as cparser


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

    # 获取config.ini
    @staticmethod
    def get_conf(section, key):
        try:
            data = Utils.get_file("Resources", "config.ini")
            return data.get(section, key)
        except Exception as e:
            print e

    @staticmethod
    def get_conf_list(section, key):
        st = Utils.get_conf(section, key)
        try:
            li = st.strip(',').split(',')
            return li
        except Exception as e:
            print e

    # 获取property文件
    @staticmethod
    def get_file(*path):
        file_path = Utils.get_project_path()
        for value in path:
            file_path = os.path.join(file_path, value)
        cf = cparser.ConfigParser()
        cf.read(file_path)
        return cf

    @staticmethod
    def assert_str_in_list(st, li):
        assert st in li

    @staticmethod
    def assert_str_not_in_list(st, li):
        assert st not in li

    @staticmethod
    def assert_list_contains_str(st, li):
        val = False
        for str in li:
            if st in str:
                val = True
                break
        assert val

    @staticmethod
    def assert_str_contains_str(str_a, str_b):
        assert str_a in str_b

    @staticmethod
    def assert_str_equal_str(str_a, str_b):
        assert str_a == str_b
