#!/usr/bin/python3
# @File: 02.py
# -*- coding:utf-8 -*-
# @Author:wanghengzhi
# @Time: 2018年12月14日

for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)
