# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
'''
登陆密码：admin | 5518136qq
'''
# Register your models here.
from .models import BlogArticles
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title','auther','publish')
    list_filter = ('publish','auther')
    search_fields = ('title','body')
    raw_id_fields = ('auther',)
    date_hierarchy = 'publish'
    ordering = ['publish','auther']
admin.site.register(BlogArticles,BlogArticlesAdmin)