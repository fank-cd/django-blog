# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Comment
from django.shortcuts import render,reverse,redirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from comment.forms import CommentForm
# Create your views here.


@login_required()
def update_comment(request):

    referer = request.META.get('HTTP_REFERER',reverse('index'))
    comment_form = CommentForm(request.POST,user=request.user)
    if comment_form.is_valid():
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.save()
        return redirect(referer)
    else:
        render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})