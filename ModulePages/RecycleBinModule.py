# encoding=utf-8
# @Time    : 2018/7/16 16:59
# @Author  : Zuo Ran
# @File    : RecycleBinModule.py

from BasePage import BasePage
import os
from Utils.PropertyUtils import PropertyUtils


class RecycleBinModule(BasePage):
    __RECYCLEBIN = PropertyUtils(os.path.join("InspectPages", "RecycleBinPage.ini"))

    __recycleBin = __RECYCLEBIN.get("RECYCLEBIN")
    __all = __RECYCLEBIN.get("ALL")
    __delete = __RECYCLEBIN.get("DELETE")
    __submitDelete = __RECYCLEBIN.get("SUBMITDELETE")

    def delete_all(self):
        self.driver.click("RECYCLEBIN", locator=self.__recycleBin)
        self.driver.click("ALL", locator=self.__all)
        self.driver.click("DELETE", locator=self.__delete)
        self.driver.click("SUBMITDELETE", locator=self.__submitDelete)
