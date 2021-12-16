#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : get_yaml_data.py
# @Time     : 2021/11/30 12:30
# @Author   : yanglei
# @Software : PyCharm


import yaml

data_path = '/Users/yanglei2_vendor/Desktop/20211031/task/test_data/test_data_add.yaml'


def get_yaml_data(path):
    with open(path, 'r') as file:
        data = yaml.full_load(file.read())
    return data




