from django.shortcuts import render
from read_count.utils import get_seven_days_read_data,get_tody_hot_data,get_yesterday_hot_data
from blog.models import Blog
from django.contrib.contenttypes.models import ContentType


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(content_type=blog_content_type)


    context = {}
    context['today_hot_data'] = get_tody_hot_data(content_type=blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(content_type=blog_content_type)
    context['dates'] = dates
    context['read_nums'] = read_nums
    return render(request, 'index.html', context=context)
