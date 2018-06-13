# encoding=utf-8
# @Time    : 2018/6/8 10:33
# @Author  : Zuo Ran
# @File    : NetworkPrivateModule.py
import os
from BasePage import BasePage
from Utils.PropertyUtils import PropertyUtils
from Utils.Utils import Utils


class NetworkPrivateModule(BasePage):
    __PRIVATE = PropertyUtils(os.path.join("InspectPages", "NetworkPrivatePage.ini"))

    __network = __PRIVATE.get("NETWORK")
    __private = __PRIVATE.get("PRIVATE")
    __create = __PRIVATE.get("CREATE")
    __name = __PRIVATE.get("NAME")
    __share = __PRIVATE.get("SHARE")
    __addSubnet = __PRIVATE.get("ADDSUBNET")
    __subnetName = __PRIVATE.get("SUBNETNAME")
    __subnetSegment = __PRIVATE.get("SUBNETSEGMENT")
    __submitSubnet = __PRIVATE.get("SUBMITSUBNET")
    __submitAdd = __PRIVATE.get("SUBMITADD")
    __privateNames = __PRIVATE.get("PRIVATENAMES")
    __subnetNames = __PRIVATE.get("SUBNETWORKNAMES")
    __modifyPrivateNameButton = __PRIVATE.get("MODIFYPRIVATENAMEBUTTON")
    __modifyPrivateName = __PRIVATE.get("MODIFYPRIVATENAME")
    __modifyPrivateNameSubmit = __PRIVATE.get("MODIFYPRIVATENAMESUBMIT")
    __modifyShare = __PRIVATE.get("MODIFYSHARE")
    __privateTable = __PRIVATE.get("PRIVATETABLE")
    __privateNameTd = __PRIVATE.get("PRIVATENAMETD")
    __sharedTd = __PRIVATE.get("SHAREDTD")
    __delete = __PRIVATE.get("DELETE")
    __submitDelete = __PRIVATE.get("SUBMITDELETE")

    def create_private_network(self, data):
        self.driver.click("NETWORK", locator=self.__network)
        self.driver.click("RIVATE", locator=self.__private)
        self.driver.click("CREATE", locator=self.__create)
        self.driver.wait(1)
        self.driver.input("NAME", data["name"], locator=self.__name)
        self.driver.click("ADDSUBNET", locator=self.__addSubnet)
        self.driver.input("SUBNETNAME", data["subnet_name"], locator=self.__subnetName)
        self.driver.input("SUBNETSEGMENT", data["subnet_segment"], locator=self.__subnetSegment)
        self.driver.click("SUBMITSUBNET", locator=self.__submitSubnet)
        self.driver.click("SUBMITBUTTON", locator=self.__submitAdd)

        self.driver.wait(1)
        private_names = self.driver.get_elements_text("PRIVATENAME", locator=self.__privateNames)
        subnet_names = self.driver.get_elements_text("SUBNETNAME", self.__subnetNames)

        Utils.assert_str_in_list(data["name"], private_names)
        Utils.assert_list_contains_str(data["subnet_name"], subnet_names)
        Utils.assert_list_contains_str(data["subnet_segment"], subnet_names)

    def modify_private_network(self, data):
        self.driver.click("NETWORK", locator=self.__network)
        self.driver.click("RIVATE", locator=self.__private)
        self.driver.click("PRIVATELINK", locator="LINKTEXT:" + data["name"])
        self.driver.click("MODIFYPRIVATENAMEBUTTON", locator=self.__modifyPrivateNameButton)
        self.driver.input("MODIFYPRIVATENAME", data["name_modify"], locator=self.__modifyPrivateName)
        self.driver.click("MODIFYPRIVATENAMESUBMIT", locator=self.__modifyPrivateNameSubmit)
        self.modify_status(self.__modifyShare, "SHARED", data["share_modify"])
        self.driver.click("RIVATE", locator=self.__private)

        private_names = self.driver.get_elements_text("PRIVATENAMES", locator=self.__privateNames)
        Utils.assert_str_in_list(data["name_modify"], private_names)

        networks = self.driver.find_elements(self.__privateTable)
        for network in networks:
            if self.driver.get_text("PRIVATENAME", locator=self.__privateNameTd, element=network) == \
                    data["name_modify"]:
                Utils.assert_str_equal_str(
                    self.driver.get_text("SHAREDTD", locator=self.__sharedTd, element=network),
                    data["share_modify"])
                break

    def delete_private_network(self, data):
        self.driver.click("INFO", locator="LINKTEXT:" + data["name_modify"])
        self.driver.click("DELETESUBNET", locator=self.__delete)
        self.driver.click("SUBMITDELETE", locator=self.__submitDelete)
        self.driver.click("RIVATE", locator=self.__private)

        networks = self.driver.find_elements(self.__privateTable)
        for network in networks:
            if self.driver.get_text("PRIVATENAME", locator=self.__privateNameTd, element=network) == \
                    data["name_modify"]:
                self.driver.click("DELETEPRIVATE", locator=self.__delete, element=network)
        self.driver.click("SUBMITDELETE", locator=self.__submitDelete)

        private_names = self.driver.get_elements_text("PRIVATENAME", locator=self.__privateNames)
        Utils.assert_str_not_in_list(data["name_modify"], private_names)
