# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import ReadNum,ReadDetail
from django.contrib import admin


class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num','content_object')

class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date','read_num','content_object')


admin.site.register(ReadNum,ReadNumAdmin)
admin.site.register(ReadDetail,ReadDetailAdmin)
