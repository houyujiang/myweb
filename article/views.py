 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import ArticleColumn
from .forms import ArticleColumnForm
from django.views.decorators.http import require_POST

#栏目视图
@login_required(login_url='/account/login')
@csrf_exempt
def article_column(request):
    if request.method == 'GET':
        columns = ArticleColumn.objects.filter(user = request.user)
        column_form = ArticleColumnForm()
        return render(request,'article/column/article_column.html',{'columns':columns,'column_form':column_form})
    if request.method == 'POST':
        column_name = request.POST['column']
        columns =ArticleColumn.objects.filter(user_id=request.user.id,column = column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user,column = column_name)
            return HttpResponse('1')
#修改栏目名称视图
@login_required(login_url='account/login')
@require_POST
@csrf_exempt
def rename_column(request):
    column_name = request.POST['column_name']
    column_id = request.POST['column_id']
    print(column_id)
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.column = column_name
        line.save()
        return HttpResponse('1')
    except:
        return HttpResponse('0')


#删除栏目
@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_column(request):
    column_id = request.POST['column_id']

    try:
        line =ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse('1')
    except:
        HttpResponse('0')