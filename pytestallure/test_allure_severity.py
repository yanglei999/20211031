#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_allure_severity.py
# @Time     : 2021/11/24 19:19
# @Author   : yanglei
# @Software : PyCharm

import pytest
import allure

@allure.severity(allure.severity_level.TRIVIAL)
def test_01():
    print('01============')

@allure.severity(allure.severity_level.MINOR)
def test_02():
    print('02===========')

@allure.severity(allure.severity_level.NORMAL)
def test_03():
    print('03=================')

@allure.severity(allure.severity_level.CRITICAL)
def test_04():
    print('04==================')

@allure.severity(allure.severity_level.BLOCKER)
def test_05():
    print('05==============')


if __name__ == '__main__':
    pytest.main()
