# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,render_to_response,get_object_or_404
from .models import Blog,Tag
# Create your views here.

def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request,'blog/blog_list.html',context=context)

def blog_detail(request,pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk=pk)
    return render(request,'blog/blog_detail.html',context=context)
    #pass

def blog_with_type(request,pk):
    context = {}
    blog_type = get_object_or_404(Tag,pk=pk)
    context['blogs'] = Blog.objects.filter(tags=blog_type)
    context['blog_type'] = blog_type
    return render(request,'blog/blog_with_type.html',context=context)