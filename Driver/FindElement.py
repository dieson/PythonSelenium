# encoding=utf-8
# @Time    : 2017/12/27 11:36
# @Author  : Zuo Ran
# @File    : FindElement.py
from DriverUtils import DriverUtils
from Utils.Utils import Utils


class FindElement(DriverUtils):
    def find_elements(self, locator):
        self.wait(self.wait_time)
        locator_type = Utils.get_locator_type(locator)
        locator_str = Utils.get_locator_str(locator)
        elements = None

        try:
            if locator_type == "XPATH":
                elements = self.driver.find_elements_by_xpath(locator_str)
            elif locator_type == "ID":
                elements = self.driver.find_elements_by_id(locator_str)
            elif locator_type == "CLASS":
                elements = self.driver.find_elements_by_class_name(locator_str)
            elif locator_type == "TAGNAME":
                elements = self.driver.find_elements_by_tag_name(locator_str)
            elif locator_type == "LINKTEXT":
                elements = self.driver.find_elements_by_link_text(locator_str)
            elif locator_type == "NAME":
                elements = self.driver.find_elements_by_name(locator_str)
            elif locator_type == "CSS":
                elements = self.driver.find_elements_by_css_selector(locator_str)
            self.logger.log_successful("Find the elements")
        except Exception as e:
            self.logger.log_error("Unable get the elements")
            self.logger.log_exception(e)
        return elements

    def find_element(self, locator):
        self.wait(self.wait_time)
        locator_type = Utils.get_locator_type(locator)
        locator_str = Utils.get_locator_str(locator)
        element = None

        try:
            if locator_type == "XPATH":
                element = self.driver.find_element_by_xpath(locator_str)
            elif locator_type == "ID":
                element = self.driver.find_element_by_id(locator_str)
            elif locator_type == "CLASS":
                element = self.driver.find_element_by_class_name(locator_str)
            elif locator_type == "TAGNAME":
                element = self.driver.find_element_by_tag_name(locator_str)
            elif locator_type == "LINKTEXT":
                element = self.driver.find_element_by_link_text(locator_str)
            elif locator_type == "NAME":
                element = self.driver.find_element_by_name(locator_str)
            elif locator_type == "CSS":
                element = self.driver.find_element_by_css_selector(locator_str)
                self.logger.log_successful("Find the element")
        except Exception as e:
            self.logger.log_error("Unable get the element")
            self.logger.log_exception(e)
        return element

    def find_element_by_element(self, element, locator):
        self.wait(self.wait_time)
        locator_type = Utils.get_locator_type(locator)
        locator_str = Utils.get_locator_str(locator)
        e = None

        try:
            if locator_type == "XPATH":
                e = element.find_element_by_xpath(locator_str)
            elif locator_type == "ID":
                e = element.find_element_by_id(locator_str)
            elif locator_type == "CLASS":
                e = element.find_element_by_class_name(locator_str)
            elif locator_type == "TAGNAME":
                e = element.find_element_by_tag_name(locator_str)
            elif locator_type == "LINKTEXT":
                e = element.find_element_by_link_text(locator_str)
            elif locator_type == "NAME":
                e = element.find_element_by_name(locator_str)
            elif locator_type == "CSS":
                e = element.find_element_by_css_selector(locator_str)
                self.logger.log_successful("Find the element")
        except Exception as e:
            self.logger.log_error("Unable get the element")
            self.logger.log_exception(e)
        return e

    def exist_element(self, locator):
        self.wait(self.wait_time)
        locator_type = Utils.get_locator_type(locator)
        locator_str = Utils.get_locator_str(locator)

        try:
            if locator_type == "XPATH":
                self.driver.find_element_by_xpath(locator_str)
            elif locator_type == "ID":
                self.driver.find_element_by_id(locator_str)
            elif locator_type == "CLASS":
                self.driver.find_element_by_class_name(locator_str)
            elif locator_type == "TAGNAME":
                self.driver.find_element_by_tag_name(locator_str)
            elif locator_type == "LINKTEXT":
                self.driver.find_element_by_link_text(locator_str)
            elif locator_type == "NAME":
                self.driver.find_element_by_name(locator_str)
            elif locator_type == "CSS":
                self.driver.find_element_by_css_selector(locator_str)
            return True
        except Exception:
            return False
