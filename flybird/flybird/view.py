#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:  wanghengzhi
from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    return  HttpResponse("<p>世界好</p>")

def hello(request):
    context = {}
    context['hello'] = "Hello World !"
    return render(request,'hello.html',context)
