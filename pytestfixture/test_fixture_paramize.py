#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_fixture_paramize.py
# @Time     : 2021/11/23 19:57
# @Author   : yanglei
# @Software : PyCharm

import pytest

@pytest.mark.parametrize('test_input, expected', [("3+5", 8), ("2+5", 7), ('2+6',8)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize('x', [1,2])
@pytest.mark.parametrize('y', [8,10, 11])
def test_foo(x, y):
    print(f'测试数据组合x:{x},y:{y}')

if __name__ == '__main__':
    pytest.main()