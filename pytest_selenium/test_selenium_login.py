#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_selenium_login.py
# @Time     : 2021/12/3 10:48
# @Author   : yanglei
# @Software : PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestLogin(object):

    def setup(self):

        self.driver = webdriver.Chrome()
        self.driver.get('http://10.4.12.105:30007/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//*[@placeholder="请输入用户名"]').send_keys('admin')
        self.driver.find_element(By.XPATH, '//*[@placeholder="请输入密码"]').send_keys('root')
        self.driver.find_element(By.XPATH, '//*[@class="el-button el-button--primary login-btn"]').click()
        # time.sleep(2)

    def teardown(self):
        self.driver.quit()

    # def test_login(self):
    #     self.driver.find_element(By.XPATH, '//*[@placeholder="请输入用户名"]').send_keys('admin')
    #     self.driver.find_element(By.XPATH, '//*[@placeholder="请输入密码"]').send_keys('root')
    #     self.driver.find_element(By.XPATH, '//*[@class="el-button el-button--primary login-btn"]').click()
    #     time.sleep(10)



if __name__ == '__main__':
    pytest.main()
