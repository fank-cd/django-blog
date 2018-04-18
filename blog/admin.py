# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Tag,Blog
from django.contrib import admin

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('id','tag_name')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Tag)
admin.site.register(Blog)