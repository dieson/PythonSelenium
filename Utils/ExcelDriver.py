# encoding=utf-8
# @Time    : 2017/12/29 14:09
# @Author  : Zuo Ran
# @File    : ExcelDriver.py
import os
import xlrd
from Utils import Utils


class ExcelDriver(object):
    def __init__(self, excel_name, sheet_name):
        self.file_path = os.path.join(Utils.get_project_path(), "TestData", excel_name)
        self.data = xlrd.open_workbook(self.file_path)
        self.table = self.data.sheet_by_name(sheet_name)

        # get titles
        self.row = self.table.row_values(0)

        # get rows number
        self.row_num = self.table.nrows

        # get columns number
        self.col_num = self.table.ncols

        # the current column
        self.cur_row_no = 1

    def next(self):
        r = []
        while self.has_next():
            s = {}
            col = self.table.row_values(self.cur_row_no)
            i = self.col_num
            for x in range(i):
                s[self.row[x]] = str(col[x])
            r.append(s)
            self.cur_row_no += 1
        return r

    def has_next(self):
        if self.row_num == 0 or self.row_num <= self.cur_row_no:
            return False
        else:
            return True
