#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : test_calc_case.py
# @Time     : 2021/11/30 10:23
# @Author   : yanglei
# @Software : PyCharm

import pytest
import selenium
from selenium import webdriver
from task.common.test_calc import Calc
from task.tool.get_yaml_data import get_yaml_data

data_path = '/Users/yanglei2_vendor/Desktop/20211031/task/test_data/test_data_add.yaml'
data = get_yaml_data(data_path)
step_conf_path = "/Users/yanglei2_vendor/Desktop/20211031/task/conf/step_conf.yaml"


@pytest.fixture()
def login():
    user = "aaaa"
    print('user&&&&&&&')
    yield user
    print('denglu成功-------*******-----')


@pytest.mark.ddd
class TestCalcCase(object):

    @pytest.fixture()
    def calc(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a,b,c", data)
    @pytest.mark.add
    def test_calc_add(self, login, calc, a, b, c):
        print(f"打印：    {login}")
        step_conf_data = get_yaml_data(step_conf_path)
        print(step_conf_data, "=============")
        for step in step_conf_data:
            if step == "add":
                result = self.calc.add(a, b)
                print(result, "add----------------")
            elif step == "add1":
                result = self.calc.add1(a, b)
                print(result, 'add1-----------')
            assert c == result

        # result = self.calc.add(a, b)
        # assert result == c

    @pytest.mark.parametrize('a,b,c', [[2, 1, 1], [3, 4, -1], [0.7, 0.2, 0.5]])
    @pytest.mark.xfail
    @pytest.mark.sub
    def test_calc_sub(self, calc, a, b, c):
        result = self.calc.sub(a, b)
        assert result == c

    @pytest.mark.parametrize('a,b,c', [[1, 2, 2], [2, 2, 4], [-1, -2, 2], [0, 2, 0]])
    @pytest.mark.mult
    def test_calc_mult(self, calc, a, b, c):
        result = self.calc.mult(a, b)
        assert result == c

    @pytest.mark.parametrize('a, b, c', [[4, 2, 2], [4, -2, -2], [4, 0, 0]])
    @pytest.mark.div
    def test_calc_div(self, calc, a, b, c):
        try:
            result = self.calc.div(a, b)
        except:
            print('0不能作为被除数')
        else:
            assert result == c


if __name__ == '__main__':
    # pytest.main(['-vs','./task/test_case/test_calc_case.py'])
    pytest.main()
    # 命令行：
    # pytest ./task/test_case/test_calc_case.py -m add or sub
    # pytest --collect-only
    # pytest -k add
    # pytest -junit-xml=path   生成一个xml的文件
