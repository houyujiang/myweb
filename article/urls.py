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

]