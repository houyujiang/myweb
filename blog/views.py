# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BlogArticles
from django.shortcuts import render

# Create your views here.
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return  render(request,'blog/titles.html',{'blogs':blogs})

def blog_artitcle(request, article_id):
    article = BlogArticles.objects.get(id = article_id)
    print(article)
    pub = article.publish
    return  render(request,'blog/content.html',{'article':article,'publish':pub})