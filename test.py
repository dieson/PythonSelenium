# encoding=utf-8
# @Time    : 2017/12/26 16:38
# @Author  : Zuo Ran
# @File    : test.py
import sys
from selenium import webdriver
from Driver.DriverUtils import DriverUtils

if __name__ == '__main__':
    driver = DriverUtils()
    driver.open("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python%E8%B0%83%E7%94%A8%E7%88%B6%E7%B1%BB%E5%AF%B9%E8%B1%A1&oq=python%25E8%25B0%2583%25E7%2594%25A8%25E7%2588%25B6%25E7%25B1%25BB%25E5%258F%2598%25E9%2587%258F&rsv_pq=8ca0a1e9000098a1&rsv_t=f4a4iGQ%2BaVQoRe%2FRsIQcUD69uJd585NkHVEiif1faYq9Lixu2yG6rJvqavw&rqlang=cn&rsv_enter=1&inputT=11406&rsv_sug3=469&rsv_sug1=406&rsv_sug7=100&bs=python%E8%B0%83%E7%94%A8%E7%88%B6%E7%B1%BB%E5%8F%98%E9%87%8F")
    driver.screenshot("baidu")
    driver.sleep(3)
    driver.quit()
