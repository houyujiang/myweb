# -*- coding: utf-8 -*-
# @Time    : 2018/2/12 22:07
# @Author  : houyujiang
# @Email   : houyujiang@live.cn
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import ArticleColumn

#栏目的表单
class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)