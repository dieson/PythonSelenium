# encoding=utf-8
# @Time    : 2017/12/27 9:09
# @Author  : Zuo Ran
# @File    : DriverUtils.py
import os
import time
from Driver import Driver
from Utils.Utils import Utils


class DriverUtils(Driver):
    def wait(self, secound):
        if type(secound) is not int:
            secound = int(secound)

        try:
            time.sleep(secound)
        except Exception as e:
            self.logger.log_info(e)

    def screenshot(self, image):
        imagepath = os.path.join(Utils.get_project_path(), "Screenshot", image + ".png")
        try:
            self.driver.save_screenshot(imagepath)
            self.logger.log_info(imagepath)
        except Exception as e:
            self.logger.log_error("Screenshot")
            self.logger.log_exception(e)

    def alert_switch(self):
        alert = None
        try:
            alert = self.driver.switch_to_alert()
            self.logger.log_successful("Switch to alert")
        except Exception as e:
            self.screenshot("Alert")
            self.logger.log_error("Unable switch to alert")
            self.logger.log_exception(e)
        return alert

    def alert_accept(self):
        alert = self.alert_switch()
        try:
            alert.accept()
            self.logger.log_successful("Accept")
        except Exception as e:
            self.screenshot("Alert")
            self.logger.log_error("Unable accept")
            self.logger.log_exception(e)

    def alert_dismiss(self):
        alert = self.alert_switch()
        try:
            alert.dismiss()
            self.logger.log_successful("Dismiss")
        except Exception as e:
            self.screenshot("Alert")
            self.logger.log_error("Unable dismiss")
            self.logger.log_exception(e)

    def alert_text(self):
        text = None
        alert = self.alert_switch()
        try:
            alert.text()
            self.logger.log_successful("Get text")
        except Exception as e:
            self.screenshot("Alert")
            self.logger.log_error("Unable get text")
            self.logger.log_exception(e)
        return text

    def switch_window(self):
        try:
            handle = self.driver.current_window_handle
            self.driver.switch_to_window(handle)
            self.logger.log_successful("Switch to window")
        except Exception as e:
            self.screenshot("Alert")
            self.logger.log_error("Unable switch to window")
            self.logger.log_exception(e)
