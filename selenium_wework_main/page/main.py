#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : main.py
# @Time     : 2021/12/15 22:41
# @Author   : yanglei
# @Software : PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = 'localhost:9222'
    #     self._driver = webdriver.Chrome(options=options)
    #     self._driver.implicitly_wait(5)
    #     self._driver.get('https://work.weixin.qq.com/wework_admin/frame')

    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        # self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()

        self.find(By.ID, 'menu_contacts').click()
        sleep(2)
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddMember(self._driver)
