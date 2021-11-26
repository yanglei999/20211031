#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_allure_feature_story.py
# @Time     : 2021/11/24 16:12
# @Author   : yanglei
# @Software : PyCharm

import pytest
import allure


@allure.feature('登录模块')
class TestLogin(object):

    @allure.story('登录成功')
    def test_login1(self):
        print('success')

    @allure.story('登录失败，用户名错误')
    def test_login2(self):
        print('用户名错误登录失败')

    @allure.story('登录失败，密码错误')
    def test_login3(self):
        print('密码错误')

    @allure.story('密码缺失子功能')
    def test_login4(self):
        with allure.step('点击用户名'):
            print('输入用户名')
        with allure.step('点击密码'):
            print('输入密码')