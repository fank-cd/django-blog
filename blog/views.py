# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404
from django.db.models import Count
from .models import Blog, Tag
from read_count.utils import read_count_once_read
# Create your views here.


def get_blog_lis_common_data(request, blogs_all_list):

    page_num = request.GET.get("page", 1)
    paginator = Paginator(blogs_all_list, 5)
    page_of_blogs = paginator.page(page_num)
    current_page_num = page_of_blogs.number

    if current_page_num == 1:
        page_range = [
            current_page_num,
            current_page_num + 1,
            current_page_num + 2]

    elif current_page_num == 2:
        page_range = [
            current_page_num - 1,
            current_page_num,
            current_page_num + 1,
            current_page_num + 2]

    elif current_page_num == paginator.num_pages - 1:
        page_range = [
            current_page_num - 2,
            current_page_num - 1,
            current_page_num,
            current_page_num + 1]

    elif current_page_num == paginator.num_pages:
        page_range = [
            current_page_num - 2,
            current_page_num - 1,
            current_page_num]
    else:
        page_range = [
            current_page_num - 2,
            current_page_num - 1,
            current_page_num,
            current_page_num + 1,
            current_page_num + 2]

    blog_dates = Blog.objects.dates('create_time', 'month', order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(
            create_time__year=blog_date.year,
            create_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count
    context = {}
    context['page_range'] = page_range
    context['page_of_blogs'] = page_of_blogs
    context['blogs'] = blogs_all_list
    context['blog_tags'] = Tag.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = blog_dates_dict
    return context


def blog_list(request):

    blogs_all_list = Blog.objects.all()
    context = get_blog_lis_common_data(request, blogs_all_list)
    return render(request, 'blog/blog_list.html', context=context)


def blog_with_type(request, pk):
    context = {}
    blog_type = get_object_or_404(Tag, pk=pk)
    blogs_all_list = Blog.objects.filter(tags=blog_type)
    context = get_blog_lis_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render(request, 'blog/blog_with_type.html', context=context)


def blog_with_date(request, year, month):
    context = {}
    blogs_all_list = Blog.objects.filter(
        create_time__year=year, create_time__month=month)
    context = get_blog_lis_common_data(request, blogs_all_list)

    context['blog_with_date'] = '%s年%s月' % (year, month)

    return render(request, 'blog/blog_with_date.html', context=context)


def blog_detail(request, pk):
    context = {}
    blog = get_object_or_404(Blog, pk=pk)
    read_cookie_key = read_count_once_read(request, blog)
    context['blog'] = blog
    context['previous_blog'] = Blog.objects.filter(
        create_time__gt=blog.create_time).last()
    context['next_blog'] = Blog.objects.filter(
        create_time__lt=blog.create_time).first()
    response = render_to_response('blog/blog_detail.html', context=context)
    response.set_cookie(key=read_cookie_key, value="true", max_age=60)
    return response
   # return render(request,'blog/blog_detail.html',context=context)
