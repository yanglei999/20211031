#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : base.py
# @Time     : 2021/11/23 19:28
# @Author   : yanglei
# @Software : PyCharm

import pytest


@pytest.fixture()
def login():
    print('这是个登录方法')