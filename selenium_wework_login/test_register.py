#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_register.py
# @Time     : 2021/12/14 20:41
# @Author   : yanglei
# @Software : PyCharm
from selenium_wework_login.index import Index


class TestRegister():
    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_login().goto_register().register()
        # self.index.goto_register().register()

