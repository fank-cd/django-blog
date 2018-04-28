# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Tag, Blog
from django.contrib import admin

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'tags',
        'get_read_num',
        'create_time',
        'last_update_time')


admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
