# -*-coding:utf-8-*-
# @Time    : 2018/7/11 14:04
# @Author  : Zuo Ran
# @File    : EnterprisePorjectTest.py
import unittest

import ddt
from Driver.ElementUtils import ElementUtils
from ModulePages.EnterpriseProjectModule import EnterpriseProjectModule
from Utils.ExcelUtils import ExcelUtils


@ddt.ddt
class EnterprisePorjectTest(unittest.TestCase):
    excel = ExcelUtils("EnterpriseData.xlsx", "Project").next()
    driver = None
    project_module = None

    @classmethod
    def setUpClass(cls):
        cls.driver = ElementUtils()
        cls.project_module = EnterpriseProjectModule(cls.driver)
        cls.project_module.login_neocu()

    # @ddt.data(*excel)
    # def test_01_create_project_network(self, data):
    #     self.project_module.create_project(data)

    @ddt.data(*excel)
    def test_02_delete_project_network(self, data):
        self.project_module.delete_project(data)

    @classmethod
    def tearDownClass(cls):
        cls.project_module.quit_neocu()


if __name__ == '__main__':
    unittest.main()
