#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @File     : test_reuse_browser.py
# @Time     : 2021/12/10 12:24
# @Author   : yanglei
# @Software : PyCharm
import shelve
import time

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup(self):
        """
        解决登录问题方法（网页版企业微信，扫码登录的问题）：

        1\复用浏览器，先用命令打开调试地址：mac电脑：Google\ Chrome --remote-debugging-port=9222,windows电脑：Chrome --remote-debugging-port=9222
        命令前要保证Chrome的浏览器和进程全部关闭掉，
        2\或者是用cookies方法，
        :return:
        """
        # option = Options()
        # option.debugger_address = 'localhost:9222'
        # self.driver = webdriver.Chrome(options=option)

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_classification(self):
        # self.driver.get('https://ceshiren.com/')
        # self.driver.get('https://home.testing-studio.com/')
        # self.driver.execute_script('return document.getElementById("ember45")').click()

        # self.driver.find_element(By.XPATH, '//a[text()="热门"]').click()

        print(self.driver.get_cookies())
        # cookies = [
        #     {'domain': 'ceshiren.com', 'httpOnly': True, 'name': '_forum_session', 'path': '/', 'sameSite': 'Lax',
        #      'secure': True,
        #      'value': 'WFJiNG9JcWtBZ3hTUEpWcEV2SE9jUzYxaWpOUm5KTU5HUlZIWnU3bnRPMGRSWVVDMC95TzBDRk1hdC9VYVNFNm5LY0hORGErOXBURHI3dnhVTUpzQWFXQnRlOE5UcldFTjhHdjZia0xVajBsbzhoOHRNUDdibUJocmxocFdrcEtJWTdEK0JTdmxZaGNWZVl1MEtlK3VNWktvVEdibHhObzNtK1lQUlp5Q1p1SWppWDFhWXMzbHNhcmwvazBncUZxLS1pNE8welVVRmdnY0NHSzFtQ0VaOTJRPT0%3D--f9b84ba3749ad0a7fccfef65e716384861ad3388'},
        #     {'domain': '.ceshiren.com', 'expiry': 1670827288, 'httpOnly': False,
        #      'name': 'Hm_lvt_214f62eef822bde113f63fedcab70931', 'path': '/', 'secure': False,
        #      'value': '1639112422,1639112773,1639122430,1639291288'},
        #     {'domain': 'ceshiren.com', 'expiry': 1644475288, 'httpOnly': True, 'name': '_t', 'path': '/',
        #      'sameSite': 'Lax', 'secure': True,
        #      'value': 'QTRSWFVGbTJIUmJVeXdpV2VuaFlPZS85MFhXRFhHZzdJdGZrVUh6S280Wm5PTkMvblpQMU9kU245UHhuTVBOM1lKaUxITGNDTHpaeTcwUk8yQTJUUHp4dUdjV3FrakdEd3JWOTBlNnl4VFpIN2NkWnJBMGtaWHovUVFzVlBLT0FiQUV0dnF4TDFuWlN2UHFXOWtGWnVmU1EvYUVSSG5XSjNVR2tsbnI1K3ZYR2dxK0NydzVURXpYZmxmb1pIVFl1OVdEUTJNaElab2g1SW9rQXBNU0dYVWdRdmNUQnA5RXRSNDVwdWp1TmUwSlYzSkZoWXROS21CSVJ0WWg5dFgyNEdiWGFBYnBTdUV0QXdSNWRGeDBIL0E9PS0tTDBzR0tRVXg4UjhHQXpuU3BDRXVuQT09--1d7b19b378bd9f6e6ab3b189ab0e5defb0f3b9ee'},
        #     {'domain': '.ceshiren.com', 'httpOnly': False, 'name': 'Hm_lpvt_214f62eef822bde113f63fedcab70931',
        #      'path': '/', 'secure': False, 'value': '1639291288'},
        #     {'domain': '.ceshiren.com', 'expiry': 1639377688, 'httpOnly': False, 'name': '_gid', 'path': '/',
        #      'secure': False, 'value': 'GA1.2.785487440.1639287216'},
        #     {'domain': '.ceshiren.com', 'expiry': 1702363288, 'httpOnly': False, 'name': '_ga', 'path': '/',
        #      'secure': False, 'value': 'GA1.2.714296969.1639105485'}]

        self.driver.get('https://ceshiren.com/')

        db = shelve.open('cookies')  # shelve相当于一个小型数据库
        # 先保存cookies到db中
        # db['cookie'] = self.driver.get_cookies()

        # 获取db中的cookie值
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get('https://ceshiren.com/')

        time.sleep(5)
        db.close()


if __name__ == '__main__':
    pytest.main()
