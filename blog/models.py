# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag,blank=True,on_delete=models.DO_NOTHING,default='')
    content = models.TextField()

    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    #recommend = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-create_time']
