# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Comment
from django.shortcuts import render,reverse,redirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def update_comment(request):
    user = request.user
    referer = request.META.get('HTTP_REFERER',reverse('index'))
    text = request.POST.get('text','').strip()
    if text == '':
        return render(request,'error.html',{'message':'评论内容为空','redirect_to':referer})

    try:
        content_type = request.POST.get('content_type','')
        object_id = int(request.POST.get('object_id',''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as e:
        render(request, 'error.html', {'message': '评论对象不存在','redirect_to':referer})
    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_object = model_obj
    comment.save()


    return redirect(referer)