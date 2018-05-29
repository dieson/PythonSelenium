# encoding=utf-8
# @Time    : 2018/3/13 15:13
# @Author  : Zuo Ran
# @File    : ExternalModule.py

from Utils.PropertyUtils import PropertyUtils


class ExternalModule(object):
    __EXTERNAL = PropertyUtils("ExternalPage.properties")

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
    __submitSubnet = __EXTERNAL.get("SUBMITSUBNET")
    __submitButton = __EXTERNAL.get("SUBMITBUTTON")

    def __init__(self, driver_utils):
        self.driver = driver_utils

    def create_external_network(self, data):
        self.driver.click(self.__network, "NETWORK")
        self.driver.click(self.__external, "EXTERNAL")
        self.driver.click(self.__create, "CREATE")
        self.driver.input(self.__name, data["name"], "NAME")
        # self.driver.is_checked(self.__share, data["share"], "SHARE")
        self.driver.click(self.__submitButton, "SUBMITBUTTON")
