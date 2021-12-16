#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : add_member.py
# @Time     : 2021/12/15 21:24
# @Author   : yanglei
# @Software : PyCharm

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self._driver = driver

    def add_member(self):
        sleep(2)
        self.find(By.ID, 'username').send_keys('yanglei110')
        self.find(By.ID, 'memberAdd_acctid').send_keys('4')
        self.find(By.ID, 'memberAdd_phone').send_keys('15518776914')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(3)
        return True

    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

        list = []
        for element in elements:
            list.append(element.get_attribute('title'))

        # list = [element.get_attribute('title') for element in elements]
        # return [element.get_attribute('title') for element in elements]

        return list
