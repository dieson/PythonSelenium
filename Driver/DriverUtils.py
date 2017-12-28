# encoding=utf-8
# @Time    : 2017/12/27 9:09
# @Author  : Zuo Ran
# @File    : DriverUtils.py
import os
import time
from Driver import Driver
from Utils.Util import Util


class DriverUtils(Driver):
    def sleep(self, secound):
        try:
            time.sleep(secound)
        except Exception as e:
            print e

    def screenshot(self, image):
        imagepath = os.path.join(Util.get_project_path(), "Screenshot", image + ".png")
        try:
            self.driver.save_screenshot(imagepath)
            print imagepath
        except Exception as e:
            print e
            print "[Fail] Screenshot"

    def alert_switch(self):
        alert = None
        try:
            alert = self.driver.switch_to_alert()
            print "[Successful] Switch to alert"
        except Exception as e:
            self.screenshot("Alert")
            print "[Fail] Unable switch to alert"
            print e
        return alert

    def alert_accept(self):
        alert = self.alert_switch()
        try:
            alert.accept()
            print "[Successful] Accept"
        except Exception as e:
            self.screenshot("Alert")
            print "[Fail] Unable accept"
            print e

    def alert_dismiss(self):
        alert = self.alert_switch()
        try:
            alert.dismiss()
            print "[Successful] Dismiss"
        except Exception as e:
            self.screenshot("Alert")
            print "[Fail] Unable dismiss"
            print e

    def alert_text(self):
        text = None
        alert = self.alert_switch()
        try:
            alert.text()
            print "[Successful] Get text"
        except Exception as e:
            self.screenshot("Alert")
            print "[Fail] Unable get text"
            print e
        return text
