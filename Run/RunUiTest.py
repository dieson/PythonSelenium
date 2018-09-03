# encoding=utf-8
# @Time    : 2018/7/26 10:36
# @Author  : Zuo Ran
# @File    : RunUiTest.py
import os
import time
import unittest
import HTMLTestRunner
from Utils.Utils import Utils
from Driver.ElementUtils import ElementUtils
from ModulePages.ExternalModule import ExternalModule
from ModulePages.NetworkPrivateModule import NetworkPrivateModule
from ModulePages.EnterpriseProjectModule import EnterpriseProjectModule


def create_depend(data):
    # 创建依赖数据
    driver = ElementUtils()
    project_module = EnterpriseProjectModule(driver)
    project_module.login_neocu()
    project_module.depend_create_project(data)

    if "ExternalTest" not in Utils.get_conf_list("test", "suite"):
        external_module = ExternalModule(driver)
        external_module.depend_crate_external(data)

    private_module = NetworkPrivateModule(driver)
    private_module.depend_create_private(data)
    private_module.quit_neocu()


def delete_depend(data):
    # 清空依赖数据
    driver = ElementUtils()
    external_module = ExternalModule(driver)
    external_module.login_neocu()
    external_module.depend_delete_external(data)

    private_module = NetworkPrivateModule(driver)
    private_module.depend_delete_private(data)

    project_module = EnterpriseProjectModule(driver)
    project_module.depend_delete_project(data)
    project_module.quit_neocu()


if __name__ == '__main__':
    depend_test_data = {"project": "depend_ui_project", "description": "test", "external_name": "depend_ui_external",
                        "external_subnet": "depend_ui_subnet", "external_subnet_segment": "10.10.10.0/24",
                        "private_name": "depend_ui_private", "private_subnet": "depend_ui_subnet",
                        "private_subnet_segment": "12.12.12.0/24"}
    # 创建依赖数据
    create_depend(depend_test_data)

    # 加载测试集
    test_suite = unittest.TestSuite()

    et = "ExternalTest"
    test_list = Utils.get_conf_list("test", "suite")
    if et in test_list:
        ret = __import__("TestCases." + et, fromlist=True)
        test_suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(ret))
        test_list.remove(et)

    for test in test_list:
        ret = __import__("TestCases." + test, fromlist=True)
        test_suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(ret))

    # 生成测试报告
    report_dir = os.path.join(Utils.get_project_path(), "Report/")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = report_dir + now + '_result.html'
    fp = open(filename, 'wb')
    # 执行测试
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='NeoCU UI Test Report', description='')
    runner.run(test_suite)
    fp.close()

    # 清空依赖数据
    delete_depend(depend_test_data)
