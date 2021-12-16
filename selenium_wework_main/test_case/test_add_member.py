#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_add_member.py
# @Time     : 2021/12/15 20:58
# @Author   : yanglei
# @Software : PyCharm
from time import sleep

from selenium_wework_main.page.base_page import BasePage
from selenium_wework_main.page.main import Main


class TestAddMember(object):
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        sleep(3)
        assert "yanglei110" in add_member.get_member()