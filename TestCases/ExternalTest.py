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
    excel = ExcelUtils("ExternalData.xlsx", "External").next()
    driver = None
    external_module = None

    @classmethod
    def setUpClass(cls):
        cls.driver = BasePage()
        cls.driver.login_neocu()
        cls.external_module = ExternalModule(cls.driver)

    @ddt.data(*excel)
    def test_01_create_external_network(self, data):
        self.external_module.create_external_network(data)

    @ddt.data(*excel)
    def test_02_modify_external_network(self, data):
        self.external_module.modify_external_network(data)

    @ddt.data(*excel)
    def test_03_delete_external_network(self, data):
        self.external_module.delete_external_network(data)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit_neocu()


if __name__ == '__main__':
    unittest.main()
