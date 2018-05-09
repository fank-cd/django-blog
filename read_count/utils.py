# coding:utf-8
from django.contrib.contenttypes.models import ContentType
from .models import ReadNum, ReadDetail
from django.utils import timezone
from django.db.models import Sum
import datetime


def read_count_once_read(request, obj):
    """
    处理阅读数量，设置60s过期的cookie，如果没有cookie则阅读量+1，如果数据库还没有初始数据，则初始化。
    :param request:
    :param obj: 一般就是指blog
    :return: blog_pk_read,返回一个cookie的key值，ct.model,obj.p主要是作为分类
    """
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)
    if not request.COOKIES.get(key):
        """
        if ReadNum.objects.filter(content_type=ct,object_id=blog.pk).count():
            readnum = ReadNum.objects.get(content_type=ct,object_id=blog.pk)
        else:
            readnum = ReadNum(content_type=ct,object_id=blog.pk)
        """
        readnum = ReadNum.objects.get_or_create(
            content_type=ct, object_id=obj.pk)[0]
        readnum.read_num += 1
        readnum.save()
        date = timezone.now().date()
        readdetail = ReadDetail.objects.get_or_create(
            content_type=ct, object_id=obj.pk, date=date)[0]
        # get_or_create方法会返回一个两个值，一个是查找的元素，一个是这个元素是创建的还是获取的
        # 也可写为readdetail,created = ReadDetail.objects.get_or_create(
        # content_type=ct, object_id=obj.pk, date=date)[0]
        """
        if ReadDetail.objects.filter(content_type=ct,object_id=obj.pk,date=date).count():
            readdetail = ReadDetail.objects.get(content_type=ct,object_id=obj.pk,date=date)
        else:
            readdetail = ReadDetail(content_type=ct,object_id=obj.pk,date=date)
        """
        readdetail.read_num += 1
        readdetail.save()
    return key


def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    #today - datetime.timedelta(days=1)
    dates = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(
            content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums


def get_tody_hot_data(content_type):
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(
        content_type=content_type, date=today).order_by('-read_num')
    return read_details[:7]


def get_yesterday_hot_data(content_type):
    today = timezone.now().date()
    yesterdaty = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(
        content_type=content_type, date=yesterdaty).order_by('-read_num')
    return read_details[:7]


def get_seven_days_hot_data(content_type):
    today = timezone.now().date()
    date = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(
        content_type=content_type,
        date__lt=today,
        date__gte=date).values(
        'content_type',
        'object_id') .annotate(
            read_num_sum=Sum('read_num')). order_by('-read_num')

    return read_details[:7]
