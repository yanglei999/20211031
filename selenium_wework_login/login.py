#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : login.py
# @Time     : 2021/12/13 21:36
# @Author   : yanglei
# @Software : PyCharm
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_login.register import Register


class Login(object):
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        # click register
        self._driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self._driver)