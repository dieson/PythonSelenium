# encoding=utf-8
# @Time    : 2018/3/15 14:37
# @Author  : Zuo Ran
# @File    : NeoCUUtils.py
from ElementUtils import ElementUtils


class BasePage(ElementUtils):
    def quit_neocu(self):
        print "Logout"

        logged = self.exist_element("CSS:div.ult-usernav-toggle")
        if logged:
            self.click("CSS:div.ult-usernav", "USER NAVIGATION")
            self.click("CSS:a.ult-usernav-logout", "LOGOUT")
        self.quit()

    def wait_logo(self):
        print "Wait for the login successful"

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
