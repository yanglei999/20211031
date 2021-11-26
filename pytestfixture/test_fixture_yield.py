#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_fixture_yield.py
# @Time     : 2021/11/23 19:51
# @Author   : yanglei
# @Software : PyCharm

import pytest

@pytest.fixture(scope="module")
def open():
    print('打开浏览器')
    yield
    print('执行teardown')
    print('最后关闭浏览器')

def test_search1(open):
    print('test_search1')

def test_search2():
    print('test_search2')

def test_search3():
    print('test_search3')

if __name__ == '__main__':
    pytest.main()