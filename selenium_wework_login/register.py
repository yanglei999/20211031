#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : register.py
# @Time     : 2021/12/13 21:38
# @Author   : yanglei
# @Software : PyCharm
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register(object):
    # driver: WebDriver  ----标签的用法，和Index类中的driver结合起来
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def register(self):
        # click
        # send_keys
        time.sleep(2)
        # 公司名称
        self._driver.find_element(By.ID, "corp_name").send_keys('红红火火公司')
        self._driver.find_element(By.ID, 'manager_name').send_keys('yanglei8888888')
        time.sleep(3)
        self._driver.quit()
        return True

    def teardown(self):
        self._driver.quit()
