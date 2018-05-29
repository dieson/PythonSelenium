# encoding=utf-8
# @Time    : 2017/12/26 16:26
# @Author  : Zuo Ran
# @File    : Driver.py
import os
from selenium import webdriver
from Utils.Utils import Utils
from Utils.PropertyUtils import PropertyUtils


class Driver(object):
    def __init__(self):
        self.wait_time = PropertyUtils.get_conf().get("script", "wait_time")
        self.url = PropertyUtils.get_conf().get("serverconf", "server_url")
        self.chromeDriver = os.path.join(Utils.get_project_path(), "Resources", "chromedriver.exe")
        self.driver = webdriver.Chrome(self.chromeDriver)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def quit(self):
        try:
            self.driver.quit()
            print "[Successful] Quit the app"
        except Exception as e:
            print "[Fail] Quit the app"
            print e
            assert False

    def get_driver(self):
        return self.driver


