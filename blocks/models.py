#!coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Blocks(models.Model):
    name = models.CharField(u"板块名称",max_length=30)
    desc = models.CharField(u"板块描述",max_length=120)
    owner = models.ForeignKey(User,verbose_name=u"管理员")

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    #表示当前表,表示的含义,中文显示
    class Meta:
        verbose_name = u"板块"
        verbose_name_plural = u"板块"
