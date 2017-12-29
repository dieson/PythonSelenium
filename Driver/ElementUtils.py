# encoding=utf-8
# @Time    : 2017/12/28 10:01
# @Author  : Zuo Ran
# @File    : ElementUtils.py
from FindElement import FindElement


class ElementUtils(FindElement):
    def input(self, locator, value, elementName):
        element = self.find_element(locator)
        try:
            element.clear()
            element.send_keys(value)
            print "[Successful] " + elementName + " input:" + value
        except Exception as e:
            self.screenshot(elementName)
            print "[Fail] Unable to input"
            print e
            assert False

    def clear(self, locator, elementName):
        element = self.find_element(locator)
        try:
            element.clear()
            print "[Successful] Clear the " + elementName
        except Exception as e:
            self.screenshot(elementName)
            print "[Fail] Unable to Clear the " + elementName
            print e
            assert False

    def click(self, locator, elementName):
        try:
            self.find_element(locator).click()
            print "[Successful] Click the " + elementName
        except Exception as e:
            self.screenshot(elementName)
            print "[Fail] Unable to click"
            print e
            assert False

    def select(self, locator, value, elementName):
        element = self.find_element(locator)
        try:
            element.select_by_visible_text(value)
            print "[Successful] Select the " + value
        except Exception as e:
            self.screenshot(elementName)
            print "[Fail] Unable to select"
            print e
            assert False

    def get_text(self, locator, elementName):
        msg = None
        try:
            msg = self.find_element(locator).text()
            print "[Successful] Get the " + elementName
        except Exception as e:
            self.screenshot(elementName)
            print "[Fail] Get attribute failure"
            print e
            assert False
        return msg

    def is_displayed(self, locator, elementName):
        is_displayed = False
        try:
            is_displayed = self.find_element(locator).is_displayed()
            print "[Successful] The element is displayed"
        except Exception as e:
            self.screenshot(elementName)
            print "[Fail] The element is displayed"
            print e
            assert False
        return is_displayed
