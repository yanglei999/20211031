#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
# @File     : demo2.py
# @Time     : 2021/11/25 11:04
# @Author   : yanglei
# @Software : PyCharm


__all__ = ['hello']   # 只对外开放列表中的变量或者方法、模块等，可以写到init文件中，hello 可以被其他文件引用，但是http不能被引用

import sys

hello = 'hello world'
http = 'yanglei'

print(sys.path)