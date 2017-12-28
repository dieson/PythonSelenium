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
            print "[Successful]" + elementName + " input:" + value
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
