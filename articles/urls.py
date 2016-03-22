#coding:utf-8
from django.conf.urls import url,include

#将一个数值赋值给block_id
urlpatterns = [
        url(r'^lists/(?P<block_id>\d+)','articles.views.article_list',name='article_list'),
    ]
