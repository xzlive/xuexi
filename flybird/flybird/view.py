#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:  wanghengzhi
from django.http import HttpResponse
from django.shortcuts import render,render_to_response

def first_page(request):
    return  HttpResponse("<p>世界好</p>")

def hello(request):
    context = {}
    context['hello'] = "Hello World !"
    return render(request,'hello.html',context)

def view1(request):
    return render(request,'1.html')
def view2(request):
    return render(request,'2.html')

def views(request,url):
    if url=='view1':
        template_name='1.html'
    else:
        template_name='2.html'
    return render(request,template_name)