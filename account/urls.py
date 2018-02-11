# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 22:12
# @Author  : houyujiang
# @Email   : houyujiang@live.cn
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import  views
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    #url(r'^login/$', views.user_login, name='user_login'),
    url(r'^login/$', auth_views.login,name='user_login'),
    url(r'^new-login/$',auth_views.login,{'template_name':'account/login.html','redirect_field_name':'/blog/'}),
    #url(r'^logout/$',auth_views.logout,name='user_logout'),
    #登出
    url(r'^logout/$', auth_views.logout ,{'template_name':'account/logout.html'},name='user_logout'),
    #注册
    url(r'^register/$',views.register , name='user_register'),
    #更改密码
    url(r'^password-change/$',auth_views.password_change,
        {'post_change_redirect':'/account/password-change-done'},name='password_change'
        ),
    #更改密码后跳转
    url(r'^password-change-done/$',auth_views.password_change_done,name='password_change_done'),

    #重置密码
    url(r'^password-reset/$',auth_views.password_reset,
        {'template_name':'account/password_reset_form.html',
            'email_template_name':'account/password_reset_email.html',
            'subject_template_name':'account/password_reset_subject.txt',
            'post_reset_redirect':'/account/password-reset-done'},
                                            name='password_reset'),
    #重置后
    url(r'^password-reset-done/$', auth_views.password_reset_done,
        {'template_name':'account/password_reset_done.html'},name='password_reset_done'),
    #修改确认
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,{'template_name':'account/password_reset_confirm.html',
                                            'post_reset_redirect':'/account/password-reset-complete'},
                                            name='password_reset_confirm'),

    url(r'^password-reset-complete/$',
        auth_views.password_reset_complete, {'template_name': 'account/password_reset_complete.html'
                                            },
        name='password_reset_complete'),
    #查看个人信息
    url(r'^my-information/$',views.myself,name='my_information'),
    #编辑个人信息
    url(r'^edit-my-information/$',views.myself_edit,name='edit_my_information'),
    #查看个人照片
    url(r'^my-image/$',views.my_image,name='my_image'),
]