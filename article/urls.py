# -*- coding: utf-8 -*-
# @Time    : 2018/2/12 23:22
# @Author  : houyujiang
# @Email   : houyujiang@live.cn
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^article-cloumn/$',views.article_column,name='article_column'),
    url(r'^rename-column/$',views.rename_column,name='rename_column'),
    url(r'^del-colmun/$',views.del_column,name='del_column'),
    url(r'^article-post/$',views.article_post,name='article_post'),
    url(r'^article-list/$',views.article_list,name='article_list'),#文章标题列表
    url(r'^article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.article_detail,name='article_detail'),#显示页面详情
    url(r'^del-article/$',views.del_article,name="del_article"),#删除文章
    url(r'^redit-article/(?P<article_id>\d+)/$',views.redit_article,name="redit_article"),
]