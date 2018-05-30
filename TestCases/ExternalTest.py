# -*-coding:utf-8-*-
# @Time    : 2018/3/15 14:04
# @Author  : Zuo Ran
# @File    : ExternalTest.py
import unittest
import ddt
from Driver.BasePage import BasePage
from ModulePages.ExternalModule import ExternalModule
from Utils.ExcelUtils import ExcelUtils


@ddt.ddt
class ExternalTest(unittest.TestCase):
    excel = ExcelUtils("ExternalData.xlsx", "External")
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = BasePage()
        cls.driver.login_neocu()

    @ddt.data(*excel.next())
    def test_create_external_network(self, data):
        external_module = ExternalModule(self.driver)
        external_module.create_external_network(data)

    @classmethod
    def tearDown(cls):
        cls.driver.quit_neocu()


if __name__ == '__main__':
    unittest.main()
