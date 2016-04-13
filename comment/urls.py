#coding:utf-8
from django.conf.urls import url,include

#将一个数值赋值给block_id
urlpatterns = [
        url(r'^list/$','comment.views.comment_list',name='comment_list'),
        url(r'^create/$','comment.views.comment_create',name='comment_create'),
    ]
