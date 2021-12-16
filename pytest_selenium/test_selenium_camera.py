#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_selenium_camera.py
# @Time     : 2021/12/6 11:21
# @Author   : yanglei
# @Software : PyCharm
import time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pytest_selenium.test_selenium_login import TestLogin


class TestCamera(TestLogin):

    def test_camera(self):

        device_element = self.driver.find_element(By.XPATH, '//span[text()="设备管理"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(device_element)).click()
        # webdriver.ActionChains(self.driver).move_to_element(device_element ).click(device_element ).perform()
        self.driver.find_element(By.XPATH, '//li[@class="el-menu-item"]/p[text()="工业相机管理"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="新增相机"]').click()
        self.driver.find_element(By.XPATH, '(//div[@class="el-input el-input--suffix"]/span[@class="el-input__suffix"])[1]').click()
        self.driver.find_element(By.XPATH, '(//ul[@class="el-scrollbar__view el-select-dropdown__list"]//*[text()="面阵相机"])[1]').click()


        time.sleep(3)