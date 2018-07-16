# encoding=utf-8
# @Time    : 2018/3/15 14:58
# @Author  : Zuo Ran
# @File    : LoginModule.py
import os
from Utils.PropertyUtils import PropertyUtils
from Utils.Utils import Utils
from ModulePages.BasePage import BasePage


class LoginModule(BasePage):
    __LOGIN = PropertyUtils(os.path.join("InspectPages", "LoginPage.ini"))

    __username = __LOGIN.get("USERNAME")
    __password = __LOGIN.get("PASSWORD")
    __login_button = __LOGIN.get("LOGIN")

    def login(self):
        username = Utils.get_conf("serverconf", "username")
        password = Utils.get_conf("serverconf", "password")
        self.driver.close_notification()
        self.driver.input("UserName", username, locator=self.__username)
        self.driver.input("Password", password, locator=self.__password)
        self.driver.click("LoginButton", locator=self.__login_button)

        self.driver.wait_logo()

    def login_test(self, username, password):
        self.close_notification()
        self.driver.input("UserName", username, locator=self.__username)
        self.driver.input("Password", password, locator=self.__password)
        self.driver.click("LoginButton", locator=self.__login_button)
