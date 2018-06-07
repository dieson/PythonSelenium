# encoding=utf-8
# @Time    : 2018/3/13 15:13
# @Author  : Zuo Ran
# @File    : ExternalModule.py
import os
from Utils.PropertyUtils import PropertyUtils
from Utils.Utils import Utils


class ExternalModule(object):
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

    def __init__(self, driver_utils):
        self.driver = driver_utils

    def create_external_network(self, data):
        self.driver.click(self.__network, "NETWORK")
        self.driver.click(self.__external, "EXTERNAL")
        self.driver.click(self.__create, "CREATE")
        self.driver.wait(1)
        self.driver.input(self.__name, data["name"], "NAME")
        # self.driver.is_checked(self.__share, data["share"], "SHARE")
        self.driver.click(self.__addSubnet, "ADDSUBNET")
        self.driver.input(self.__subnetName, data["subnet_name"], "SUBNETNAME")
        self.driver.input(self.__subnetSegment, data["subnet_segment"], "SUBNETSEGMENT")
        self.driver.click(self.__submitSubnet, "SUBMITSUBNET")
        self.driver.click(self.__submitButton, "SUBMITBUTTON")

        self.driver.wait(1)
        external_names = self.driver.get_elements_text(self.__externalName, "EXTERNALNAME")
        subnet_work_names = self.driver.get_elements_text(self.__subnetWorkName, "SUBNETWORKNAME")

        Utils.assert_str_in_list(data["name"], external_names)
        Utils.assert_list_contains_str(data["subnet_name"], subnet_work_names)
        Utils.assert_list_contains_str(data["subnet_segment"], subnet_work_names)

    def modify_external_network(self, data):
        self.driver.click("LINKTEXT:" + data["name"], "EXTERNALLINK")
        self.driver.click(self.__modifyNetworkNameButton, "MODIFYNETWORKNAMEBUTTON")
        self.driver.input(self.__modifyNetworkName, data["name_modify"], "MODIFYNETWORKNAME")
        self.driver.click(self.__submitModifyNetworkName, "SUBMITMODIFYNETWORK")
        self.driver.modify_status(self.__share, "SHARED", data["share_modify"])
        self.driver.modify_status(self.__enabled, "ENABLE", data["enable_modify"])
        self.driver.click(self.__external, "EXTERNAL")

        external_names = self.driver.get_elements_text(self.__externalName, "EXTERNALNAME")
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
        self.driver.click("LINKTEXT:" + data["name_modify"], "INFO")
        self.driver.click(self.__delete, "DELETESUBNET")
        self.driver.click(self.__submitDelete, "SUBMITDELETE")
        self.driver.click(self.__external, "EXTERNAL")
        self.driver.click(self.__delete, "DELETEEXTERNAL")
        self.driver.click(self.__submitDelete, "SUBMITDELETE")

        external_names = self.driver.get_elements_text(self.__externalName, "EXTERNALNAME")
        Utils.assert_str_not_in_list(data["name_modify"], external_names)
