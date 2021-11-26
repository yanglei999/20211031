#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_autouse.py
# @Time     : 2021/11/23 19:45
# @Author   : yanglei
# @Software : PyCharm

import pytest

@pytest.fixture(autouse=True)
def open():
    print('打开浏览器')

def test_search1():
    print('test_search1')
    raise NameError
    pass

def test_search2():
    print('test_search2')
    pass

def test_search3():
    print('test_search3')
    pass


if __name__ == '__main__':
    pytest.main()
