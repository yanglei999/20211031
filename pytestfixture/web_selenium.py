#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : web_selenium.py
# @Time     : 2021/12/2 12:48
# @Author   : yanglei
# @Software : PyCharm
import time

import selenium
from selenium import webdriver

def test_a():
    driver = webdriver.Chrome()
    # driver.get('https://www.baidu.com/')
    driver.get('http://10.4.12.105:30007/login')
    # driver.get('http://10.4.12.105:30007/device/camera')
    time.sleep(3)