# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 22:40
# @Author  : houyujiang
# @Email   : houyujiang@live.cn
# @File    : forms.py
# @Software: PyCharm
from django import forms

class LoginFrom(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)