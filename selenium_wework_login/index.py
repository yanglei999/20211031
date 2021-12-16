#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : index.py
# @Time     : 2021/12/13 21:33
# @Author   : yanglei
# @Software : PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_wework_login.login import Login
from selenium_wework_login.register import Register


class Index(object):
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')
        self._driver.implicitly_wait(5)

    def goto_login(self):
        # click login
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self._driver)

    def goto_register(self):
        # click register
        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)
