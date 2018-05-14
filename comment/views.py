# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from .models import Comment
from django.contrib.auth.decorators import login_required
from comment.forms import CommentForm
from comment.utils import date_to_string
# Create your views here.


@login_required()
def update_comment(request):
    data = {}
    comment_form = CommentForm(request.POST,user=request.user)
    if comment_form.is_valid():
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']

        parent = comment_form.cleaned_data['parent']
        if not parent is None:
            comment.root = parent.root if not parent.root is None else parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()

        data['status'] = 'SUCCESS'
        data['username'] = comment.user.username
        data['comment_time'] = date_to_string(comment.comment_time.strftime('%Y-%m-%d %H:%M:%S'))
        data['text'] =comment.text
        data['content_type'] = ContentType.objects.get_for_model(comment).model
        if not  parent is None:
            data['reply_to'] = comment.reply_to.username
        else:
            data['reply_to'] = ''
        data['pk'] = comment.pk
        data['root_pk'] = comment.root.pk if not comment.root is None else ''
    else:
        data['status'] = "ERROR"
        data['message'] =list(comment_form.errors.values())[0][0]
        #render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})

    return JsonResponse(data)