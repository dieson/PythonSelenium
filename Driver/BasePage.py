# encoding=utf-8
# @Time    : 2018/3/15 14:37
# @Author  : Zuo Ran
# @File    : NeoCUUtils.py
from ElementUtils import ElementUtils
from Utils.Utils import Utils


class BasePage(ElementUtils):
    def login_neocu(self):
        username = Utils.get_conf("serverconf", "username")
        password = Utils.get_conf("serverconf", "password")
        self.close_notification()
        self.input("NAME:username", username, "UserName")
        self.input("NAME:password", password, "Password")
        self.click("CSS:.ult-btn.ult-btn-primary.ult-btn-medium", "LoginButton")

        self.wait_logo()
        self.switch_window()

    def quit_neocu(self):
        self.logger.log_info("Logout")

        logged = self.exist_element("CSS:div.ult-usernav-toggle")
        if logged:
            self.click("CSS:div.ult-usernav", "USER NAVIGATION")
            self.click("CSS:a.ult-usernav-logout", "LOGOUT")
        self.quit()

    def wait_logo(self):
        self.logger.log_info("Wait for the login successful")

        i = 0
        while self.exist_element("CSS:.login-board") is True:
            self.wait(1)
            if i < 10:
                i += 1
            else:
                break

    def close_notification(self):
        if self.exist_element("NAME:noNotify"):
            self.click("CSS:.ult-checkbox-inner.ult-checkbox-type", "NO NOTIFY")
            self.click("XPATH://div[contains(@class, 'ult-ui-dialog')]/div[2]/div/button[1]", "CLOSE")

    def modify_status(self, locator, element_name, status):
        attribute = self.get_attribute(locator, element_name, "class")
        if "ult-switch-checked" in attribute:
            if status is False or status == "false" or status == "False" or status == "FALSE" or status == "否":
                self.click(locator, element_name)
        else:
            if status is True or status == "true" or status == "True" or status == "TRUE" or status == "是":
                self.click(locator, element_name)
