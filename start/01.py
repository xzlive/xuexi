#!/usr/bin/python3
# @File: 01.py
# -*- coding:utf-8 -*-
# @Author:wanghengzhi
# @Time: 2018年12月13日

for c in open(r'E:\web-site\xuexi\start\readme.txt', 'r').readlines() :
    open(r'E:\web-site\xuexi\start\readme1.txt', 'a+').write(c)
    print(c)
else:
    print("end")
