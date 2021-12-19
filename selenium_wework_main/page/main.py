#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : main.py
# @Time     : 2021/12/15 22:41
# @Author   : yanglei
# @Software : PyCharm
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
        # 通讯录
        sleep(2)
        self.find(By.ID, 'menu_contacts').click()

        # target = expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="js_contacts172"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]'))
        # WebDriverWait(self._driver, 10).until(target).click()

        # 通讯录——添加成员
        # locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()

        # self.wait_for_click((By.CSS_SELECTOR, '.js_btn_save'))
        sleep(3)
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        # sleep(3)
        return AddMember(self._driver)
