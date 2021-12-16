#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : base.py
# @Time     : 2021/12/6 11:26
# @Author   : yanglei
# @Software : PyCharm
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBase(object):

    def setup(self):
        """
        浏览器兼容性，执行.py文件时可以直接命令： browser=firefox pytest .....py
        :return:
        """
        browser = os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.WPEWebKit()
        elif browser == 'safari':
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


# def test_login():
#     """
#     登录
#     :return:
#     """
#     driver = webdriver.Chrome()
#     driver.get('http://10.4.12.105:30007/login')
#     driver.maximize_window()
#     driver.implicitly_wait(3)
#     driver.find_element(By.XPATH, '//*[@placeholder="请输入用户名"]').send_keys('admin')
#     driver.find_element(By.XPATH, '//*[@placeholder="请输入密码"]').send_keys('root')
#     driver.find_element(By.XPATH, '//*[@class="el-button el-button--primary login-btn"]').click()
#
#     yield driver
#     driver.quit()




