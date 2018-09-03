# encoding=utf-8
# @Time    : 2017/12/26 16:26
# @Author  : Zuo Ran
# @File    : Driver.py
import os
import platform
from selenium import webdriver
from Utils.Utils import Utils
from Utils.LoggerUtils import LoggerUtils


class Driver(object):
    def __init__(self):
        self.logger = LoggerUtils()
        self.wait_time = Utils.get_conf("script", "wait_time")
        self.url = Utils.get_conf("serverconf", "server_url")
        if "Win" in platform.system():
            self.chromedriver = os.path.join(Utils.get_project_path(), "Resources", "chromedriver.exe")
        else:
            self.chromedriver = os.path.join(Utils.get_project_path(), "Resources", "chromedriver")
        self.driver = webdriver.Chrome(self.chromedriver)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def open_url(self, path):
        url = '%s%s' % (self.url, path)
        try:
            self.driver.get(url)
            self.logger.log_successful("Open the " + url)
        except Exception as e:
            self.logger.log_error("Open the " + url)
            self.logger.log_exception(e)
            assert False

    def quit(self):
        try:
            self.driver.quit()
            self.logger.log_successful("Quit the app")
        except Exception as e:
            self.logger.log_error("Quit the app")
            self.logger.log_exception(e)
            assert False

    def get_driver(self):
        return self.driver


