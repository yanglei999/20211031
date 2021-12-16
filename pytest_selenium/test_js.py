#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_js.py
# @Time     : 2021/12/8 19:52
# @Author   : yanglei
# @Software : PyCharm
import time

from selenium.webdriver.common.by import By

from pytest_selenium.base import TestBase
import pytest


class TestBaiDu(TestBase):

    def test_baidu(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.execute_script('return document.getElementById("kw")').send_keys("selenium测试")

        self.driver.execute_script('return document.getElementById("su")').click()
        # bdbutton = self.driver.execute_script('return document.getElementById("su")')
        # bdbutton.click()

        self.driver.execute_script('document.documentElement.scrollTop=10000')
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="page"]/div/a[10]').click()
        time.sleep(5)



