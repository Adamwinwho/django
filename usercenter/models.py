#coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ActivateCode(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'用户')
    code = models.CharField(u'激活码',max_length=100)

    expire_timestamp = models.DateTimeField()

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)
