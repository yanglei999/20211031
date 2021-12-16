#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : base_page.py
# @Time     : 2021/12/16 20:40
# @Author   : yanglei
# @Software : PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    _driver = None
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != '':
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

