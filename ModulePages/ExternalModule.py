# encoding=utf-8
# @Time    : 2018/3/13 15:13
# @Author  : Zuo Ran
# @File    : ExternalModule.py
import os
from BasePage import BasePage
from Utils.PropertyUtils import PropertyUtils
from Utils.Utils import Utils


class ExternalModule(BasePage):
    __EXTERNAL = PropertyUtils(os.path.join("InspectPages", "ExternalPage.ini"))

    __network = __EXTERNAL.get("NETWORK")
    __external = __EXTERNAL.get("EXTERNAL")
    __create = __EXTERNAL.get("CREATE")
    __name = __EXTERNAL.get("NAME")
    __vlanID = __EXTERNAL.get("VLANID")
    __enable = __EXTERNAL.get("ENABLE")
    __share = __EXTERNAL.get("SHARE")
    __inSubnet = __EXTERNAL.get("INSUBNET")
    __addSubnet = __EXTERNAL.get("ADDSUBNET")
    __subnetName = __EXTERNAL.get("SUBNETNAME")
    __subnetSegment = __EXTERNAL.get("SUBNETSEGMENT")
    __submitSubnet = __EXTERNAL.get("SUBMITSUBNET")
    __submitButton = __EXTERNAL.get("SUBMITBUTTON")
    __externalName = __EXTERNAL.get("EXTERNALNAME")
    __subnetWorkName = __EXTERNAL.get("SUBNETWORKNAME")
    __modifyNetworkNameButton = __EXTERNAL.get("MODIFYNETWORKNAMEBUTTON")
    __modifyNetworkName = __EXTERNAL.get("MODIFYNETWORKNAME")
    __submitModifyNetworkName = __EXTERNAL.get("SUBMITMODIFYNETWORK")
    __shared = __EXTERNAL.get("SHARED")
    __enabled = __EXTERNAL.get("ENABLED")
    __networkTable = __EXTERNAL.get("NETWORKTABLE")
    __sharedTd = __EXTERNAL.get("SHAREDTD")
    __enableTd = __EXTERNAL.get("ENABLEDTD")
    __delete = __EXTERNAL.get("DELETE")
    __submitDelete = __EXTERNAL.get("SUBMITDELETE")

    def create_external_network(self, data):
        self.driver.click("NETWORK", locator=self.__network)
        self.driver.click("EXTERNAL", locator=self.__external)
        self.driver.click("CREATE", locator=self.__create)
        self.driver.wait(1)
        self.driver.input("NAME", data["name"], locator=self.__name)
        self.driver.click("ADDSUBNET", locator=self.__addSubnet)
        self.driver.input("SUBNETNAME", data["subnet_name"], locator=self.__subnetName)
        self.driver.input("SUBNETSEGMENT", data["subnet_segment"], locator=self.__subnetSegment)
        self.driver.click("SUBMITSUBNET", locator=self.__submitSubnet)
        self.driver.click("SUBMITBUTTON", locator=self.__submitButton)

        self.driver.wait(1)
        external_names = self.driver.get_elements_text("EXTERNALNAME", locator=self.__externalName)
        subnet_work_names = self.driver.get_elements_text("SUBNETWORKNAME", locator=self.__subnetWorkName)

        Utils.assert_str_in_list(data["name"], external_names)
        Utils.assert_list_contains_str(data["subnet_name"], subnet_work_names)
        Utils.assert_list_contains_str(data["subnet_segment"], subnet_work_names)

    def modify_external_network(self, data):
        self.driver.click("EXTERNALLINK", locator="LINKTEXT:" + data["name"])
        self.driver.click("MODIFYNETWORKNAMEBUTTON", locator=self.__modifyNetworkNameButton)
        self.driver.input("MODIFYNETWORKNAME", data["name_modify"], locator=self.__modifyNetworkName)
        self.driver.click("SUBMITMODIFYNETWORK", locaotr=self.__submitModifyNetworkName, )
        self.driver.modify_status(self.__shared, "SHARED", data["share_modify"])
        self.driver.modify_status(self.__enabled, "ENABLE", data["enable_modify"])
        self.driver.click("EXTERNAL", locator=self.__external)

        external_names = self.driver.get_elements_text("EXTERNALNAME", locator=self.__externalName)
        Utils.assert_str_in_list(data["name_modify"], external_names)

        networks = self.driver.find_elements(self.__networkTable)
        for network in networks:
            if self.driver.get_text("EXTERNALNAME", locator=self.__externalName, element=network) == \
                    data["name_modify"]:
                Utils.assert_str_equal_str(
                    self.driver.get_text("SHAREDTD", locator=self.__sharedTd, element=network),
                    data["share_modify"])
                Utils.assert_str_equal_str(
                    self.driver.get_text("ENABLEDTD", locator=self.__enableTd, element=network),
                    data["enable_modify"])
                break

    def delete_external_network(self, data):
        self.driver.click("INFO", locator="LINKTEXT:" + data["name_modify"])
        self.driver.click("DELETESUBNET", locaotr=self.__delete)
        self.driver.click("SUBMITDELETE", locator=self.__submitDelete)
        self.driver.click("EXTERNAL", locator=self.__external)
        self.driver.click("DELETEEXTERNAL", locaotr=self.__delete)
        self.driver.click("SUBMITDELETE", locator=self.__submitDelete)

        external_names = self.driver.get_elements_text("EXTERNALNAME", locator=self.__externalName)
        Utils.assert_str_not_in_list(data["name_modify"], external_names)
