# encoding=utf-8
# @Time    : 2017/12/27 11:36
# @Author  : Zuo Ran
# @File    : FindElement.py
from DriverUtils import DriverUtils
from Utils.Utils import Utils


class FindElement(DriverUtils):
    def find_element(self, locator):
        locatorType = Utils.get_locator_type(locator)
        locatorStr = Utils.get_locator_str(locator)
        element = None

        try:
            if locatorType == "XPATH":
                element = self.driver.find_element_by_xpath(locatorStr)
            elif locatorType == "ID":
                element = self.driver.find_element_by_id(locatorStr)
            elif locatorType == "CLASS":
                element = self.driver.find_element_by_class_name(locatorStr)
            elif locatorType == "TAGNAME":
                element = self.driver.find_element_by_tag_name(locatorStr)
            elif locatorType == "LINKTEXT":
                element = self.driver.find_element_by_link_text(locatorStr)
            elif locatorType == "NAME":
                element = self.driver.find_element_by_name(locatorStr)
            elif locatorType == "CSS":
                element = self.driver.find_element_by_css_selector(locatorStr)
            print "[Successful] Find the element"
        except Exception as e:
            print "[Fail] Unable get the element"
            print e
        return element

    def find_elements(self, locator):
        locatorType = Utils.get_locator_type(locator)
        locatorStr = Utils.get_locator_str(locator)
        elements = None

        try:
            if locatorType == "XPATH":
                elements = self.driver.find_element_by_xpath(locatorStr)
            elif locatorType == "ID":
                elements = self.driver.find_element_by_id(locatorStr)
            elif locatorType == "CLASS":
                elements = self.driver.find_element_by_class_name(locatorStr)
            elif locatorType == "TAGNAME":
                elements = self.driver.find_element_by_tag_name(locatorStr)
            elif locatorType == "LINKTEXT":
                elements = self.driver.find_element_by_link_text(locatorStr)
            elif locatorType == "NAME":
                elements = self.driver.find_element_by_name(locatorStr)
            elif locatorType == "CSS":
                elements = self.driver.find_element_by_css_selector(locatorStr)
            print "[Successful] Find the element"
        except Exception as e:
            print "[Fail] Unable get the element"
            print e
        return elements
