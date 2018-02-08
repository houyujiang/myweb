# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 22:40
# @Author  : houyujiang
# @Email   : houyujiang@live.cn
# @File    : forms.py
# @Software: PyCharm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
#登陆表单
class LoginFrom(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
#注册表单
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password do not match.')
        return cd['password2']

#个人信息注册表单
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','birth')
