# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from likes.models import LikeCount,LikeRecord
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


def ErrorResponse(code,message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['message'] =message
    return JsonResponse(data)

def SuccessResponse(like_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['liked_num'] = like_num

    return JsonResponse(data)

#@login_required()
def like_change(request):

    user = request.user
    if not user.is_authenticated:
        return ErrorResponse(1400, 'you were not login')


    content_type = request.GET.get('content_type')
    object_id = request.GET.get('object_id')

    try:
        content_type = ContentType.objects.get(model=content_type)
        model_class = content_type.model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except ObjectDoesNotExist:
        return ErrorResponse(1401, 'object not exist')

    if request.GET.get('is_like') == 'true':
        like_record,created=LikeRecord.objects.get_or_create(content_type=content_type,object_id=object_id,user=user)
        if created:
            like_count ,created = LikeCount.objects.get_or_create(content_type=content_type,object_id=object_id)
            like_count.like_num +=1
            like_count.save()
            return SuccessResponse(like_count.like_num)
        else:
            #未点赞过，不能重复点赞，
            return ErrorResponse(1402,'you have liked')
    else:
        #取消点赞
        if LikeRecord.objects.filter(content_type=content_type,object_id=object_id,user=user).exists():
            like_record=LikeRecord.objects.get(content_type=content_type, object_id=object_id, user=user)
            like_record.delete()
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            if not created:
                like_count.like_num -=1
                like_count.save()
                return SuccessResponse(like_count.like_num)
            else:
                return ErrorResponse(1404,'data error')
        else:
            return ErrorResponse(1403,'you have been not liked')