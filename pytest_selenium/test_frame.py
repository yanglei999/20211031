#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_frame.py
# @Time     : 2021/12/7 17:52
# @Author   : yanglei
# @Software : PyCharm
import time

from selenium.webdriver.common.by import By

from pytest_selenium.base import TestBase


class TestFrame(TestBase):

    def test_frame(self):
        """
        frame框架
        :return:
        """
        self.driver.get("https://www.runoob.com/try/runcode.php?filename=helloworld&type=bash")
        self.driver.switch_to.frame("iframeResult")  # 未嵌套的frame用switch_to.frame(),嵌套
        print(self.driver.find_element(By.XPATH, '//body[text()="Hello World !"]').text)

        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        time.sleep(2)
