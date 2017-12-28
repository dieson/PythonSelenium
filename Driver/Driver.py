# encoding=utf-8
# @Time    : 2017/12/26 16:26
# @Author  : Zuo Ran
# @File    : Driver.py
import os
from selenium import webdriver
from Utils.Util import Util


class Driver(object):
    def __init__(self):
        self.chromedriver = os.path.join(Util.get_project_path(), "Resources", "chromedriver.exe")
        self.driver = webdriver.Chrome(self.chromedriver)
        self.driver.maximize_window()

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

    def open(self, url):
        self.driver.get(url)
