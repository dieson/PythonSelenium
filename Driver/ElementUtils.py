# encoding=utf-8
# @Time    : 2017/12/28 10:01
# @Author  : Zuo Ran
# @File    : ElementUtils.py
from FindElement import FindElement


class ElementUtils(FindElement):
    def input(self, element_name, value, locator=None, element=None):
        try:
            if element is None and locator is not None:
                element = self.find_element(locator)
                element.send_keys(value)
            elif locator is None and element is not None:
                element.send_keys(value)
            elif locator is not None and element is not None:
                element = self.find_element_by_element(element, locator)
                element.send_keys(value)
            self.logger.log_successful(element_name + " input:" + value)
        except Exception as e:
            self.screenshot(element_name)
            self.logger.log_error("Unable to input")
            self.logger.log_exception(e)
            assert False

    def clear(self, element_name, locator=None, element=None):
        try:
            if element is None and locator is not None:
                self.find_element(locator).clear()
            elif locator is None and element is not None:
                element.clear()
            elif locator is not None and element is not None:
                self.find_element_by_element(element, locator).clear()
            self.logger.log_successful("Clear the " + element_name)
        except Exception as e:
            self.screenshot(element_name)
            self.logger.log_error("Unable to Clear the " + element_name)
            self.logger.log_exception(e)
            assert False

    def click(self, element_name, locator=None, element=None):
        try:
            if element is None and locator is not None:
                self.find_element(locator).click()
            elif locator is None and element is not None:
                element.click()
            elif locator is not None and element is not None:
                self.find_element_by_element(element, locator).click()
            self.logger.log_successful("Click the " + element_name)
        except Exception as e:
            self.screenshot(element_name)
            self.logger.log_error("Unable to click the " + element_name)
            self.logger.log_exception(e)
            assert False

    def select(self, element_name, value, locator=None):
        element = self.find_element(locator)
        try:
            element.select_by_visible_text(value)
            self.logger.log_successful("Select the " + value)
        except Exception as e:
            self.screenshot(element_name)
            self.logger.log_error("[Fail] Unable to select ")
            self.logger.log_exception(e)
            assert False

    def get_text(self, element_name, locator=None, element=None):
        msg = None
        try:
            if element is None and locator is not None:
                msg = self.find_element(locator).text
            elif locator is None and element is not None:
                msg = element.text
            elif locator is not None and element is not None:
                e = self.find_element_by_element(element, locator)
                msg = e.text
            self.logger.log_successful("Get the " + element_name + " '" + msg + "'")
        except Exception as e:
            self.screenshot(element_name)
            self.logger.log_error("Get attribute failure ")
            self.logger.log_exception(e)
            assert False
        return msg

    def get_elements_text(self, elements_name, locator=None, element=None):
        msg = []
        try:
            if element is None and locator is not None:
                elements = self.find_elements(locator)
                for element in elements:
                    msg.append(element.text)
            elif locator is None and element is not None:
                for el in element:
                    msg.append(el.text)
            self.logger.log_successful("Get the " + elements_name + " " + str(msg))
        except Exception as e:
            self.screenshot(elements_name)
            self.logger.log_error("Get attribute failure ")
            self.logger.log_exception(e)
            assert False
        return msg

    def is_displayed(self, locator, element_name):
        is_displayed = False
        exist = self.exist_element(locator)
        if exist:
            self.logger.log_successful("The " + element_name + " is displayed ")
            is_displayed = True
        else:
            self.logger.log_error("The " + element_name + " is not displayed ")
        return is_displayed

    def is_checked(self, locator, isCheck, element_name):
        try:
            is_checked = self.find_element(locator).get_attribute("value")
            if is_checked != isCheck:
                self.find_element(locator).click()
                self.logger.log_successful("Swicth the " + element_name)
        except Exception as e:
            self.screenshot(element_name)
            self.logger.log_error("Swicth the " + element_name)
            self.logger.log_exception(e)

    def is_existed(self, locator, element_name):
        is_exist = False
        try:
            if self.exist_element(locator):
                self.logger.log_successful(element_name + " is existed")
                is_exist = True
            else:
                self.logger.log_successful(element_name + " is not existed")
        except Exception as e:
            self.screenshot(element_name)
            self.logger.log_error(element_name + "is existed ")
            self.logger.log_exception(e)
        return is_exist

    def get_attribute(self, locator, element_name, attribute):
        element = self.find_element(locator)
        msg = None

        try:
            msg = element.get_attribute(attribute)
            self.logger.log_successful(element_name + " attribute:" + msg)
        except Exception as e:
            self.screenshot(element_name)
            self.logger.log_error("Unable to get attribute")
            self.logger.log_exception(e)
            assert False
        return msg
