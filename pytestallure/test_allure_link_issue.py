#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_allure_link_issue.py
# @Time     : 2021/11/24 17:35
# @Author   : yanglei
# @Software : PyCharm

import pytest
import allure


@allure.link('www.baidu.com', '这是哦用例中加的百度链接')
def test_login1():
    print('denglu成功')

test_case =  'http://www.baidu.com'
@allure.testcase(test_case, '这是另一条测试用例的链接地址')
def test_login2():
    print('denglu失败')

# --allure-link-pattern=issue:http://www.baidu.com/issue/{}
@allure.issue('140', '这是一个issue')
def test_login3():
    print('这是关联了一个bug')


if __name__ == '__main__':
    pytest.main()