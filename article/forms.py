# -*- coding: utf-8 -*-
# @Time    : 2018/2/12 22:07
# @Author  : houyujiang
# @Email   : houyujiang@live.cn
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import ArticleColumn,ArticlePost

#栏目的表单
class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)


#文章内容表单

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title','body')