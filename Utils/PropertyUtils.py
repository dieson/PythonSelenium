# encoding=utf-8
# @Time    : 2017/12/29 14:37
# @Author  : Zuo Ran
# @File    : PropertyUtils.py
import os
from Utils import Utils


class PropertyUtils(object):
    def __init__(self, file_name):
        self.file_path = os.path.join(Utils.get_project_path(), file_name)
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
