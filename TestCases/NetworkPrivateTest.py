# -*-coding:utf-8-*-
# @Time    : 2018/6/08 14:04
# @Author  : Zuo Ran
# @File    : ExternalTest.py
import unittest

import ddt
from Driver.ElementUtils import ElementUtils
from ModulePages.NetworkPrivateModule import NetworkPrivateModule
from Utils.ExcelUtils import ExcelUtils


@ddt.ddt
class NetworkPrivateTest(unittest.TestCase):
    excel = ExcelUtils("NetworkData.xlsx", "Private").next()
    driver = None
    private_module = None

    @classmethod
    def setUpClass(cls):
        cls.driver = ElementUtils()
        cls.private_module = NetworkPrivateModule(cls.driver)
        cls.private_module.login_neocu()

    # @ddt.data(*excel)
    # def test_01_create_private_network(self, data):
    #     self.private_module.create_private_network(data)

    @ddt.data(*excel)
    def test_02_modify_private_network(self, data):
        self.private_module.modify_private_network(data)

    @ddt.data(*excel)
    def test_03_delete_private_network(self, data):
        self.private_module.delete_private_network(data)

    @classmethod
    def tearDownClass(cls):
        cls.private_module.quit_neocu()


if __name__ == '__main__':
    unittest.main()
