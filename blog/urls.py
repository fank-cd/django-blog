from django.conf.urls import url
from . import views


urlpatterns = [url(r'^(?P<pk>[0-9]+)/$',
                   views.blog_detail,
                   name='blog_detail'),
               url(r'^$',
                   views.blog_list,
                   name="blog_list"),
               url(r'^tags/(?P<pk>[0-9]+)/$',
                   views.blog_with_type,
                   name="blog_with_type"),
               url(r'^date/(?P<year>[0-9]+)/(?P<month>[0-9]+)$',
                   views.blog_with_date,
                   name="blog_with_date"),
               ]
