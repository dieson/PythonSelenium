# encoding=utf-8
# @Time    : 2018/7/13 11:05
# @Author  : Zuo Ran
# @File    : VolumeModule.py
from BasePage import BasePage
import os
from Utils.PropertyUtils import PropertyUtils
from Utils.Utils import Utils


class VolumeModule(BasePage):
    __VOLUME = PropertyUtils(os.path.join("InspectPages", "VolumePage.ini"))

    __volume = __VOLUME.get("VOLUME")
    __create = __VOLUME.get("CREATE")
    __project = __VOLUME.get("PROJECT")
    __dataDisk = __VOLUME.get("DATADISK")
    __systemDisk = __VOLUME.get("SYSTEMDISK")
    __name = __VOLUME.get("NAME")
    __type = __VOLUME.get("TYPE")
    __capacity = __VOLUME.get("CAPACITY")
    __number = __VOLUME.get("NUMBER")
    __sharedVolume = __VOLUME.get("SHAREDVOLUME")
    __description = __VOLUME.get("DESCRIPTION")
    __okButton = __VOLUME.get("OKBUTTON")
    __volumeTable = __VOLUME.get("VOLUMETABLE")
    __checkBoxTd = __VOLUME.get("CHECKBOXTD")
    __projectTd = __VOLUME.get("PROJECTTD")
    __nameTd = __VOLUME.get("NAMETD")
    __typeTd = __VOLUME.get("TYPETD")
    __capacityTd = __VOLUME.get("CAPACITYTD")
    __capabilityTd = __VOLUME.get("CAPABILITYTD")
    __stateTd = __VOLUME.get("STATETD")
    __actions = __VOLUME.get("ACTIONS")
    __expand = __VOLUME.get("EXPAND")
    __setRw = __VOLUME.get("SETRW")
    __nameExpand = __VOLUME.get("NAMEEXPAND")
    __capacityExpand = __VOLUME.get("CAPACITYEXPAND")
    __readIopsRw = __VOLUME.get("READIOPSRW")
    __writeIopsRw = __VOLUME.get("WRITEIOPSRW")
    __readThoughput = __VOLUME.get("READTHROUGHPUT")
    __writeThoughput = __VOLUME.get("WRITETHROUGHPUT")
    __projectInfo = __VOLUME.get("PROJECTINFO")
    __nameInfo = __VOLUME.get("NAMEINFO")
    __stateInfo = __VOLUME.get("STATEINFO")
    __capabilityInfo = __VOLUME.get("CAPABILITYINFO")
    __descriptionInfo = __VOLUME.get("DESCRIPTIONINFO")
    __typeInfo = __VOLUME.get("TYPEINFO")
    __readIopsInfo = __VOLUME.get("READIOPSINFO")
    __writeIopsInfo = __VOLUME.get("WRITEIOPSINFO")
    __readThroughputInfo = __VOLUME.get("READTHROUGHPUTINFO")
    __writeThroughputInfo = __VOLUME.get("WRITETHROUGHPUTINFO")
    __submitDialog = __VOLUME.get("SUBMITDIALOG")
    __delete = __VOLUME.get("DELETE")
    __submitDelete = __VOLUME.get("SUBMITDELTE")

    def create_volume(self, data):
        self.driver.click("VOLUME", locator=self.__volume)
        self.driver.click("CREATE", locator=self.__create)
        self.driver.click("PROJECT", locator=self.__project)
        self.driver.click("PROJECT", locator="XPATH://li[contains(text(),'" + data["project"] + "')]")
        self.driver.click("DATADISK", locator=self.__dataDisk)
        self.driver.input("NAME", data["name"], locator=self.__name)
        self.driver.click("TYPE", locator=self.__type)

        type_value = ("XPATH://li[contains(text(),'" + data["type"] + "')]").decode("gb2312")
        self.driver.click("TYPE", locator=type_value)
        self.driver.clear("CAPACITY", locator=self.__capacity)
        print data["capacity"]
        self.driver.input("CAPACITY", data["capacity"], locator=self.__capacity)
        self.driver.clear("NUMBER", locator=self.__number)
        print data["number"]
        self.driver.input("NUMBER", data["number"], locator=self.__number)
        self.select_checkbox(self.__sharedVolume, "SHAREDVOLUME", data["shared"])
        self.driver.input("DESCRIPTION", data["description"], locator=self.__description)
        self.driver.click("OKBUTTON", locator=self.__okButton)

        volumes = self.driver.find_elements(self.__volumeTable)
        for volume in volumes:
            if self.driver.get_text("NAMETD", locator=self.__nameTd, element=volume) == \
                    data["name"]:
                Utils.assert_str_equal_str(
                    self.driver.get_text("PROJECTTD", locator=self.__projectTd, element=volume),
                    data["project"])
                Utils.assert_str_equal_str(
                    self.driver.get_text("TYPETD", locator=self.__typeTd, element=volume),
                    data["type"])
                Utils.assert_str_equal_str(
                    self.driver.get_text("CAPACITYTD", locator=self.__capacityTd, element=volume),
                    data["capacity"])
                Utils.assert_str_equal_str(
                    self.driver.get_text("CAPABILITYTD", locator=self.__capabilityTd, element=volume),
                    data["capability"])
                Utils.assert_str_equal_str(
                    self.driver.get_text("STATETD", locator=self.__stateTd, element=volume),
                    data["state"])
                self.driver.click("NAMETD", locator=self.__nameTd)
                break

        Utils.assert_str_equal_str(self.driver.get_text("PROJECTINFO", locator=self.__projectInfo), data["project"])
        Utils.assert_str_equal_str(self.driver.get_text("NAMEINFO", locator=self.__nameInfo), data["name"])
        Utils.assert_str_equal_str(self.driver.get_text("STATEINFO", locator=self.__stateInfo), data["state"])
        Utils.assert_str_equal_str(self.driver.get_text("CAPABILITYINFO", locator=self.__capabilityInfo),
                                   data["capability"])
        Utils.assert_str_equal_str(self.driver.get_text("DESCRIPTIONINFO", locator=self.__descriptionInfo),
                                   data["description"])
        Utils.assert_str_equal_str(self.driver.get_text("TYPEINFO", locator=self.__typeInfo), data["type"])

    def expand(self, data):
        self.driver.click("VOLUME", locator=self.__volume)

        volumes = self.driver.find_elements(self.__volumeTable)
        for volume in volumes:
            if self.driver.get_text("NAMETD", locator=self.__nameTd, element=volume) == data["name"]:
                self.driver.click("ACTIONS", locator=self.__actions, element=volume)
                self.driver.click("EXPAND", locator=self.__expand)

                Utils.assert_str_equal_str(
                    self.driver.get_text("NAMEEXPAND", locator=self.__nameExpand, element=volume), data["name"])

                self.driver.clear("CAPACITYEXPAND", locator=self.__capacityExpand)
                self.driver.input("CAPACITYEXPAND", data["capacity_expand"], locator=self.__capacityExpand)
                self.driver.click("SUBMITDIALOG", locator=self.__submitDialog)
                break

        volumes = self.driver.find_elements(self.__volumeTable)
        for volume in volumes:
            if self.driver.get_text("NAMETD", locator=self.__nameTd, element=volume) == data["name"]:
                Utils.assert_str_equal_str(
                    self.driver.get_text("CAPACITYTD", locator=self.__capacityTd, element=volume),
                    data["capacity_expand"])
                break

    def set_rw(self, data):
        self.driver.click("VOLUME", locator=self.__volume)

        volumes = self.driver.find_elements(self.__volumeTable)
        for volume in volumes:
            if self.driver.get_text("NAMETD", locator=self.__nameTd, element=volume) == data["name"]:
                self.driver.click("ACTIONS", locator=self.__actions, element=volume)
                self.driver.click("SETRW", locator=self.__setRw)
                self.driver.clear("READIOPSRW", locator=self.__readIopsRw)
                self.driver.input("READIOPSRW", data["read_iops"], locator=self.__readIopsRw)
                self.driver.clear("WRITEIOPSRW", locator=self.__writeIopsRw)
                self.driver.input("WRITEIOPSRW", data["write_iops"], locator=self.__writeIopsRw)
                self.driver.clear("READTHROUGHPUT", locator=self.__readThoughput)
                self.driver.input("READTHROUGHPUT", data["read_throughput"], locator=self.__readThoughput)
                self.driver.clear("WRITETHROUGHPUT", locator=self.__writeThoughput)
                self.driver.input("WRITETHROUGHPUT", data["write_throughput"], locator=self.__writeThoughput)
                self.driver.click("SUBMITDIALOG", locator=self.__submitDialog)
                break

        volumes = self.driver.find_elements(self.__volumeTable)
        for volume in volumes:
            if self.driver.get_text("NAMETD", locator=self.__nameTd, element=volume) == data["name"]:
                self.driver.click("NAMETD", locator=self.__nameTd)
                break

        Utils.assert_str_equal_str(self.driver.get_text("READIOPSINFO", locator=self.__readIopsInfo), data["read_iops"])
        Utils.assert_str_equal_str(self.driver.get_text("WRITEIOPSINFO", locator=self.__writeIopsInfo),
                                   data["write_iops"])
        Utils.assert_str_equal_str(self.driver.get_text("READTHROUGHPUTINFO", locator=self.__readThroughputInfo),
                                   data["read_throughput"])
        Utils.assert_str_equal_str(self.driver.get_text("WRITETHROUGHPUTINFO", locator=self.__writeThroughputInfo),
                                   data["write_throughput"])

    def delete_volume(self, data):
        self.driver.click("VOLUME", locator=self.__volume)

        volumes = self.driver.find_elements(self.__volumeTable)
        for volume in volumes:
            if self.driver.get_text("NAMETD", locator=self.__nameTd, element=volume) == data["name"]:
                self.driver.click("ACTIONS", locator=self.__actions, element=volume)
                self.driver.click("DELETE", locator=self.__delete)
                self.driver.click("SUBMITDELTE", locator=self.__submitDelete)
                break
