# encoding=utf-8
# @Time    : 2018/5/30 10:34
# @Author  : Zuo Ran
# @File    : LoggerUtils.py
import logging
import logging.config
import os
from Utils import Utils


class LoggerUtils(object):
    def __init__(self):
        filepath = os.path.join(Utils.get_project_path(), "Resources", "logging.conf")
        logging.config.fileConfig(filepath)
        self.logger = logging.getLogger("test")

    def log_info(self, buf):
        self.logger.info(buf)

    def log_error(self, buf):
        buf = "%s%s" % ("[Fail] ", buf)
        self.logger.error(buf)

    def log_successful(self, buf):
        buf = "%s%s" % ("[Successful] ", buf)
        self.log_info(buf)

    def log_exception(self, e):
        self.logger.exception(e)
