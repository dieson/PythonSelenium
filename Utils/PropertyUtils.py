# encoding=utf-8
# @Time    : 2017/12/29 14:37
# @Author  : Zuo Ran
# @File    : PropertyUtils.py
import os
from Utils import Utils
import configparser as cparser


class PropertyUtils(object):
    def __init__(self, file_name):
        self.file_path = os.path.join(Utils.get_project_path(), "InspectPages", file_name)
        self.properties = {}
        try:
            fopen = open(self.file_path, 'r')
            for line in fopen:
                line = line.strip()
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception as e:
            raise e
        else:
            fopen.close()

    def get(self, key):
        value = ""
        try:
            value = self.properties[key]
        except Exception as e:
            print e
        return value

    # 获取config.ini
    @staticmethod
    def get_conf():
        return PropertyUtils.get_file("Resources", "config.ini")

    # 获取property文件
    @staticmethod
    def get_file(*path):
        file_path = Utils.get_project_path()
        for value in path:
            file_path = os.path.join(file_path, value)
        cf = cparser.ConfigParser()
        cf.read(file_path)
        return cf
