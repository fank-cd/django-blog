# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse,render_to_response,get_object_or_404
from .models import Blog,Tag
# Create your views here.

def blog_list(request):
    page_num = request.GET.get("page",1)

    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list,5)
    page_of_blogs = paginator.page(page_num)
    current_page_num  = page_of_blogs.number

    if current_page_num == 1:
        page_range = [current_page_num, current_page_num + 1,current_page_num + 2]

    elif current_page_num == 2:
        page_range = [current_page_num-1,current_page_num, current_page_num + 1,current_page_num + 2]

    elif current_page_num ==paginator.num_pages-1:
        page_range = [current_page_num - 2, current_page_num - 1,current_page_num,current_page_num+1]

    elif current_page_num ==paginator.num_pages:
        page_range = [current_page_num - 2, current_page_num - 1, current_page_num]
    else:
        page_range =[current_page_num - 2 ,current_page_num - 1 ,current_page_num ,current_page_num + 1,current_page_num + 2]

    context = {}
    context['page_range'] = page_range
    #context['paginator'] = paginator
    context['page_of_blogs'] = page_of_blogs
    #context['blogs'] = page_of_blogs.object_list
    context['blog_tags'] = Tag.objects.all()
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
    context['blog_tags'] = Tag.objects.all()
    context['blog_type'] = blog_type
    return render(request,'blog/blog_with_type.html',context=context)