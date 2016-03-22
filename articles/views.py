#coding:utf-8
from django.shortcuts import render_to_response
from blocks.models import Blocks
from models import Article

# Create your views here.

#block_id是从urls.py中取得,是字符串类型
def article_list(request,block_id):
    block_id = int(block_id)
    block = Blocks.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")

    return render_to_response("article_list.html",{"articles":articles,"block":block})
