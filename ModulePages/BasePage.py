# encoding=utf-8
# @Time    : 2018/3/15 14:37
# @Author  : Zuo Ran
# @File    : NeoCUUtils.py
from Driver.ElementUtils import ElementUtils
from Utils.Utils import Utils


class BasePage(object):
    def __init__(self, driver_utils):
        self.driver = driver_utils

    def login_neocu(self):
        username = Utils.get_conf("serverconf", "username")
        password = Utils.get_conf("serverconf", "password")
        self.close_notification()
        self.driver.input("UserName", username, locator="NAME:username")
        self.driver.input("Password", password, locator="NAME:password")
        self.driver.click("LoginButton", locator="CSS:.ult-btn.ult-btn-primary.ult-btn-medium")

        self.wait_logo()
        self.driver.switch_window()

    def quit_neocu(self):
        self.driver.logger.log_info("Logout")

        logged = self.driver.exist_element("CSS:div.ult-usernav-toggle")
        if logged:
            self.driver.click("USER NAVIGATION", locator="CSS:div.ult-usernav")
            self.driver.click("LOGOUT", locator="CSS:a.ult-usernav-logout")
        self.driver.quit()

    def wait_logo(self):
        self.driver.logger.log_info("Wait for the login successful")

        i = 0
        while self.driver.exist_element("CSS:.login-board") is True:
            self.driver.wait(1)
            if i < 10:
                i += 1
            else:
                break

    def close_notification(self):
        if self.driver.exist_element("NAME:noNotify"):
            self.driver.click("NO NOTIFY", locator="CSS:.ult-checkbox-inner.ult-checkbox-type")
            self.driver.click("CLOSE", locator="XPATH://div[contains(@class, 'ult-ui-dialog')]/div[2]/div/button[1]")

    def select_checkbox(self, locator, element_name, status):
        attribute = self.driver.get_attribute(locator, element_name, "class")
        if "ult-switch-checked" in attribute:
            if status is False or status == "false" or status == "False" or status == "FALSE" or status == "否":
                self.driver.click(element_name, locator=locator)
        else:
            if status is True or status == "true" or status == "True" or status == "TRUE" or status == "是":
                self.driver.click(element_name, locator=locator)
