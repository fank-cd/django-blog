# coding:utf-8
from django.shortcuts import render, redirect
from read_count.utils import get_seven_days_read_data, get_tody_hot_data, get_yesterday_hot_data, get_seven_days_hot_data
from blog.models import Blog
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import datetime
from django.db.models import Sum
from django.core.cache import cache
from blog_mysql.forms import LoginForm
from django.contrib import auth
from django.urls import reverse


def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects.filter(
        read_details__date__lt=today,
        read_details__date__gte=date) .values(
        'id',
        'title') .annotate(
            read_num_sum=Sum('read_details__read_num')) .order_by('-read_num_sum')
    return blogs[:7]


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(content_type=blog_content_type)

    # 获取7天热门文章的缓存数据
    hot_blogs_for_7_days = cache.get('hot_blogs_for_7_days')
    if hot_blogs_for_7_days is None:
        hot_blogs_for_7_days = get_7_days_hot_blogs()
        cache.set('hot_blogs_for_7_days', hot_blogs_for_7_days, 3600)
        print 'caculate'
    else:
        print "use cache"

    context = {}
    context['seven_days_hot_data'] = get_7_days_hot_blogs()
    context['today_hot_data'] = get_tody_hot_data(
        content_type=blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(
        content_type=blog_content_type)
    context['dates'] = dates
    context['read_nums'] = read_nums
    return render(request, 'index.html', context=context)


def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('index')))
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context=context)
