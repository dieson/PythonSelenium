# encoding=utf-8
# @Time    : 2017/12/28 10:01
# @Author  : Zuo Ran
# @File    : ElementUtils.py
from FindElement import FindElement


class ElementUtils(FindElement):
    def input(self, locator, value, elementName):
        element = self.find_element(locator)
        try:
            # element.clear()
            element.send_keys(value)
            self.logger.log_successful(elementName + " input:" + value)
        except Exception as e:
            self.screenshot(elementName)
            self.logger.log_error("Unable to input")
            self.logger.log_exception(e)
            assert False

    def clear(self, locator, elementName):
        element = self.find_element(locator)
        try:
            element.clear()
            self.logger.log_successful("Clear the " + elementName)
        except Exception as e:
            self.screenshot(elementName)
            self.logger.log_error("Unable to Clear the " + elementName)
            self.logger.log_exception(e)
            assert False

    def click(self, locator, elementName):
        try:
            self.find_element(locator).click()
            self.logger.log_successful("Click the " + elementName)
        except Exception as e:
            self.screenshot(elementName)
            self.logger.log_error("Unable to click the " + elementName)
            self.logger.log_exception(e)
            assert False

    def select(self, locator, value, elementName):
        element = self.find_element(locator)
        try:
            element.select_by_visible_text(value)
            self.logger.log_successful("Select the " + value)
        except Exception as e:
            self.screenshot(elementName)
            self.logger.log_error("[Fail] Unable to select ")
            self.logger.log_exception(e)
            assert False

    def get_text(self, locator, elementName):
        msg = None
        try:
            msg = self.find_element(locator).text()
            self.logger.log_successful("Get the " + elementName)
        except Exception as e:
            self.screenshot(elementName)
            self.logger.log_error("Get attribute failure ")
            self.logger.log_exception(e)
            assert False
        return msg

    def is_displayed(self, locator, elementName):
        is_displayed = False
        exist = self.exist_element(locator)
        if exist:
            self.logger.log_successful("The " + elementName + " is displayed ")
            is_displayed = True
        else:
            self.logger.log_error("The " + elementName + " is not displayed ")
        return is_displayed

    def is_checked(self, locator, isCheck, elementName):
        try:
            is_checked = self.find_element(locator).get_attribute("value")
            if is_checked != isCheck:
                self.find_element(locator).click()
                self.logger.log_successful("Swicth the " + elementName)
        except Exception as e:
            self.screenshot(elementName)
            self.logger.log_error("Swicth the " + elementName)
            self.logger.log_exception(e)
