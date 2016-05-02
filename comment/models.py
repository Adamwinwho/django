#coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from articles.models import Article
from blocks.models import Blocks

# Create your models here.

class Comment(models.Model):
    #评论所属的板块,优点是直接可以查看所属板块的评论
    block = models.ForeignKey(Blocks,verbose_name=u"所属板块")
    #评论所属的文章,其实通过这个是可以获取到所属板块的
    article = models.ForeignKey(Article,verbose_name=u"所属名称")
    owner = models.ForeignKey(User,verbose_name=u"评论者")
    #评论别人的评论
    to_comment_id = models.IntegerField(u'回复评论',default=0)
    content = models.CharField(u"内容",max_length=10000)
    status = models.IntegerField(u"状态",choices=((0,u'普通'),(1,'删除')),default=0)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    @property
    def to_comment(self):
        if not self.to_comment_id:
            return None
        else:
            return Comment.objects.get(owner=self.to_comment_id)

    def __unicode__(self):
        return self.content[:20]

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'

