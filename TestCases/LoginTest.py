# -*-coding:utf-8-*-
# @Time    : 2018/3/15 14:59
# @Author  : Zuo Ran
# @File    : LoginTest.py
import unittest
import ddt
from Utils.ExcelUtils import ExcelUtils
from Driver.BasePage import BasePage
from ModulePages.LoginModule import LoginModule


@ddt.ddt
class LoginTest(unittest.TestCase):
    excel = ExcelUtils("Login.xlsx", "Login")
    driver = None
    login = None

    @classmethod
    def setUp(cls):
        cls.driver = BasePage()
        cls.login = LoginModule(cls.driver)

    @ddt.data(*excel.next())
    def test_login(self, data):
        print data
        self.login.login_test(data["USERNAME"], data["PASSWORD"])

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
