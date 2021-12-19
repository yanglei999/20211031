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
        # sleep(2)
        self.find(By.ID, 'username').send_keys('yanglei112')
        self.find(By.ID, 'memberAdd_acctid').send_keys('5')
        self.find(By.ID, 'memberAdd_phone').send_keys('15518776915')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        # sleep(3)
        return True

    def get_member(self):
        # self.wait_for_click((By.CSS_SELECTOR, '.ww_checkbox'))
        # elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # list = []
        # for element in elements:
        #     list.append(element.get_attribute('title'))
        # return list

        # list = [element.get_attribute('title') for element in elements]
        # return [element.get_attribute('title') for element in elements]


        self.wait_for_click((By.CSS_SELECTOR, '.ww_checkbox'))
        list = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                list.append(element.get_attribute('title'))
            content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            cur_page, total_page = [int(i) for i in content.split('/', 1)]
            cur_page = [int(i) for i in content.split('/', 1)][0]
            if cur_page == total_page:
                return list
            else:
                self.find(By.CSS_SELECTOR, '.js_next_page').click()

    def update_page(self):
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        return [int(i) for i in content.split('/', 1)]

    def get_member_youhua(self, value):

        self.wait_for_click((By.CSS_SELECTOR, '.ww_checkbox'))
        cur_page, total_page = self.update_page()
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                if value == element.get_attribute('title'):
                    return True
            cur_page = self.update_page()[0]
            if cur_page == total_page:
                return False
            else:
                self.find(By.CSS_SELECTOR, '.js_next_page').click()







