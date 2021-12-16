#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : run.py
# @Time     : 2021/12/1 12:47
# @Author   : yanglei
# @Software : PyCharm
from unicodedata import decimal
from decimal import Decimal

import pytest


@pytest.fixture()
def login():
    user = "aaaa"
    print('user&&&&&&&')
    yield user
    print('denglu成功-------*******-----')


def test_a(login):
    print('dddddddd')


# a = Decimal('0.4') + Decimal('0.4')
# print(Decimal(a))