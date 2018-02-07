# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      urls
   Description :
   Author :        houyujiang
   date：           2018/2/7 14:39
   IDE:             PyCharm
-------------------------------------------------
   Change Activity:
                   2018/2/7:
-------------------------------------------------
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.blog_title,name='blog_title'),
    url(r'(?P<article_id>\d)/$',views.blog_artitcle,name='blog_detail')
]