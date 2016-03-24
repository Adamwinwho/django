#coding:utf-8
from django.conf.urls import url,include

#将一个数值赋值给block_id
urlpatterns = [
        url(r'^lists/(?P<block_id>\d+)','articles.views.article_list',name='article_list'),
        url(r'^detail/(?P<article_id>\d+)','articles.views.article_detail',name='article_detail'),
        url(r'^create/(?P<block_id>\d+)','articles.views.article_create',name='article_create'),
    ]
