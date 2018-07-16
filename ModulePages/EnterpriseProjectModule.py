# encoding=utf-8
# @Time    : 2018/7/11 13:23
# @Author  : Zuo Ran
# @File    : EnterpriseProjectModule.py
import os
from BasePage import BasePage
from Utils.PropertyUtils import PropertyUtils
from Utils.Utils import Utils


class EnterpriseProjectModule(BasePage):
    __PROJECT = PropertyUtils(os.path.join("InspectPages", "EnterpriseProjectPage.ini"))

    __enterprise = __PROJECT.get("ENTERPRISE")
    __project = __PROJECT.get("PROJECT")
    __create = __PROJECT.get("CREATE")
    __name = __PROJECT.get("NAME")
    __description = __PROJECT.get("DESCRIPTION")
    __okButton = __PROJECT.get("OKBUTTON")
    __projectTr = __PROJECT.get("PROJECTTR")
    __checkboxTd = __PROJECT.get("CHECKBOXTD")
    __nameTd = __PROJECT.get("NAMETD")
    __descriptionTd = __PROJECT.get("DESCRIPTIONTD")
    __prjectAdminTd = __PROJECT.get("PROJECTADMINTD")
    __userCountTd = __PROJECT.get("USERCOUNTTD")
    __enableTd = __PROJECT.get("ENABLETD")
    __delete = __PROJECT.get("DELETE")
    __submitDelete = __PROJECT.get("SUBMITDELTE")
    __actions = __PROJECT.get("ACTIONS")
    __actionsDelete = __PROJECT.get("ACTIONSDELETE")
    __home = __PROJECT.get("HOME")

    def create_project(self, data):
        self.driver.click("ENTERPRISE", locator=self.__enterprise)
        self.driver.click("CREATE", locator=self.__create)
        self.driver.input("NAME", data["name"], locator=self.__name)
        self.driver.input("DESCRIPTION", data["description"], locator=self.__description)
        self.driver.click("OKBUTTON", locator=self.__okButton)

        projects = self.driver.find_elements(self.__projectTr)
        nameTd = self.driver.find_elements(self.__nameTd)
        descriptionTd = self.driver.find_elements(self.__descriptionTd)
        projectAdminTd = self.driver.find_elements(self.__prjectAdminTd)
        userCountTd = self.driver.find_elements(self.__userCountTd)
        enableTd = self.driver.find_elements(self.__enableTd)
        isCheck = False
        for i in range(len(projects)):
            if data["name"] in self.driver.get_text("PROJECT", element=projects[i]):
                Utils.assert_str_equal_str(
                    self.driver.get_text("NAME", element=nameTd[i]),
                    data["name"])
                Utils.assert_str_equal_str(
                    self.driver.get_text("DESCRIPTIONTD", element=descriptionTd[i]),
                    data["description"])
                Utils.assert_str_equal_str(
                    self.driver.get_text("PROJECTADMINTD", element=projectAdminTd[i]),
                    data["project_admin"])
                Utils.assert_str_equal_str(
                    self.driver.get_text("USERCOUNTTD", element=userCountTd[i]),
                    data["user_count"])
                Utils.assert_str_equal_str(
                    self.driver.get_text("ENABLETD", element=enableTd[i]),
                    data["enable"])
                isCheck = True
                break
            i += i
        if isCheck is not True:
            assert False

    def depend_create_project(self, data):
        self.driver.click("ENTERPRISE", locator=self.__enterprise)
        self.driver.click("CREATE", locator=self.__create)
        self.driver.input("NAME", data["project"], locator=self.__name)
        self.driver.input("DESCRIPTION", data["description"], locator=self.__description)
        self.driver.click("OKBUTTON", locator=self.__okButton)
        self.driver.click("HOME", locator=self.__home)

    def delete_project(self, data):
        self.driver.click("ENTERPRISE", locator=self.__enterprise)
        self.driver.click("PROJECT", locator=self.__project)

        projects = self.driver.find_elements(self.__projectTr)
        actionses = self.driver.find_elements(self.__actions)

        for i in range(len(projects)):
            if data["name"] in self.driver.get_text("PROJECT", element=projects[i]):
                self.driver.click("ACTIONS", element=actionses[i])
                self.driver.click("ACTIONSDELETE", locator=self.__actionsDelete)
                self.driver.click("SUBMITDELTE", locator=self.__submitDelete)
                break
            i += i

        assert self.driver.is_existed("LINKTEXT:" + data["name"], "PROJECTNAME") is False