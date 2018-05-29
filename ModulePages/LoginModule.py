# encoding=utf-8
# @Time    : 2018/3/15 14:58
# @Author  : Zuo Ran
# @File    : LoginModule.py
from Utils.PropertyUtils import PropertyUtils


class LoginModule(object):
    __LOGIN = PropertyUtils("LoginPage.properties")

    __username = __LOGIN.get("USERNAME")
    __password = __LOGIN.get("PASSWORD")
    __login_button = __LOGIN.get("LOGIN")

    def __init__(self, driver_utils):
        self.driver = driver_utils

    def login(self):
        username = PropertyUtils.get_conf().get("serverconf", "username")
        password = PropertyUtils.get_conf().get("serverconf", "password")
        self.driver.close_notification()
        self.driver.input(self.__username, username, "UserName")
        self.driver.input(self.__password, password, "Password")
        self.driver.click(self.__login_button, "LoginButton")

        self.driver.wait_logo()

    def login_test(self, username, password):
        self.driver.close_notification()
        self.driver.input(self.__username, username, "UserName")
        self.driver.input(self.__password, password, "Password")
        self.driver.click(self.__login_button, "LoginButton")
