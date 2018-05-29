# encoding=utf-8
# @Time    : 2017/12/26 16:26
# @Author  : Zuo Ran
# @File    : Driver.py
import os
from selenium import webdriver
from Utils.Utils import Utils
import platform


class Driver(object):
    def __init__(self):
        self.wait_time = Utils.get_conf("script", "wait_time")
        self.url = Utils.get_conf("serverconf", "server_url")
        if "Win" in platform.system():
            self.chromedriver = os.path.join(Utils.get_project_path(), "Resources", "chromedriver.exe")
        else:
            self.chromedriver = os.path.join(Utils.get_project_path(), "Resources", "chromedriver")
        self.driver = webdriver.Chrome(self.chromedriver)
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


