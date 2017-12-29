# encoding=utf-8
# @Time    : 2017/12/29 15:19
# @Author  : Zuo Ran
# @File    : DemoModule.py
from Driver.ElementUtils import ElementUtils
from Utils.PropertyUtils import PropertyUtils


class DemoModule(object):
    __DEMO = PropertyUtils("DemoLocator.properties")

    __username = __DEMO.get("USERNAME")
    __password = __DEMO.get("PASSWORD")
    __login_button = __DEMO.get("LOGIN")

    def __init__(self, driver_utils):
        self.driver = driver_utils

    def login(self, username, password):
        self.driver.input(self.__username, username, "UserName")
        self.driver.input(self.__password, password, "Password")
        self.driver.click(self.__login_button, "LoginButton")
