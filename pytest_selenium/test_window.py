#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_window.py
# @Time     : 2021/12/7 11:04
# @Author   : yanglei
# @Software : PyCharm
import time

from selenium.webdriver.common.by import By

from pytest_selenium.base import TestBase


class TestBaiDu(TestBase):

    def test_baidu(self):
        """
        窗口切换
        :return:
        """
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.CSS_SELECTOR, '[id="s-top-loginbtn"]').click()
        win = self.driver.current_window_handle
        print(win)
        self.driver.find_element(By.CSS_SELECTOR, '[id="TANGRAM__PSP_11__regLink"]').click()
        print(self.driver.current_window_handle)
        win_list = self.driver.window_handles
        print(self.driver.window_handles)
        self.driver.switch_to.window(win_list[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys('yanglei')
        time.sleep(2)


