# -*-coding:utf-8-*-
# @Time    : 2017/12/29 15:35
# @Author  : Zuo Ran
# @File    : DemoModule.py
import unittest
import ddt
from Utils.ExcelDriver import ExcelDriver
from Driver.ElementUtils import ElementUtils
from PageModules.DemoModule import DemoModule


@ddt.ddt
class DemoTest(unittest.TestCase):
    excel = ExcelDriver("Login.xlsx", "Login")
    driver = None
    demo = None

    @classmethod
    def setUp(cls):
        cls.driver = ElementUtils("https://10.130.96.20/auth/login/?next=/platformproject/")
        cls.demo = DemoModule(cls.driver)

    @ddt.data(*excel.next())
    def test_something(self, data):
        print data
        self.demo.login(data["USERNAME"], data["PASSWORD"])

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
