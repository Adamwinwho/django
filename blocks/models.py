#!coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Blocks(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=120)
    owner = models.ForeignKey(User,verbose_name=u"管理员")

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

