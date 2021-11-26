#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_allure_attach.py
# @Time     : 2021/11/24 19:49
# @Author   : yanglei
# @Software : PyCharm

import pytest
import allure

def test_attach_text():
    print('text------------')
    allure.attach('这是一个纯文本====', attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach('<body>这是一个html的body</body>', 'html测试块', attachment_type=allure.attachment_type.HTML)
    print('html------------')