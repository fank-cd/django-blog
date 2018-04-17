# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    descript = models.TextField()

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name

class Blog(models.Model):
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag,blank=True)
    content = models.TextField()

    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    recommend = models.BooleanField(default=True)

    def __unicode__(self):
        return self.caption,self.author,self.publish_time
    class Meta:
        ordering = ['-publish_time']
