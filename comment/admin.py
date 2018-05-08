# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from comment.models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','content_type','text','comment_time','user')

admin.site.register(Comment, CommentAdmin)
