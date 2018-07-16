# -*-coding:utf-8-*-
# @Time    : 2018/7/16 9:48
# @Author  : Zuo Ran
# @File    : VolumeTest.py
import unittest

import ddt
from Driver.ElementUtils import ElementUtils
from ModulePages.VolumeModule import VolumeModule
from ModulePages.EnterpriseProjectModule import EnterpriseProjectModule
from ModulePages.RecycleBinModule import RecycleBinModule
from Utils.ExcelUtils import ExcelUtils


@ddt.ddt
class VolumeTest(unittest.TestCase):
    excel = ExcelUtils("StorageData.xlsx", "Volume").next()
    driver = None
    volume_module = None
    project_module = None

    @classmethod
    def setUpClass(cls):
        cls.driver = ElementUtils()
        cls.volume_module = VolumeModule(cls.driver)
        cls.volume_module.login_neocu()

        cls.project_module = EnterpriseProjectModule(cls.driver)
        cls.project_module.depend_create_project(cls.excel[0])

    @ddt.data(*excel)
    def test_01_create_volume(self, data):
        self.volume_module.create_volume(data)

    @ddt.data(*excel)
    def test_02_expand(self, data):
        self.volume_module.expand(data)

    @ddt.data(*excel)
    def test_03_set_rw(self, data):
        self.volume_module.set_rw(data)

    @ddt.data(*excel)
    def test_04_delete_volume(self, data):
        self.volume_module.delete_volume(data)

    @classmethod
    def tearDownClass(cls):
        recycleBin = RecycleBinModule(cls.driver)
        recycleBin.delete_all()

        cls.project_module.delete_project(cls.excel[0])


if __name__ == '__main__':
    unittest.main()
