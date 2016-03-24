#coding:utf-8
from django.shortcuts import render_to_response,redirect
from blocks.models import Blocks
from models import Article
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your views here.

#block_id是从urls.py中取得,是字符串类型
def article_list(request,block_id):
    block_id = int(block_id)
    block = Blocks.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")

    return render_to_response("article_list.html",{"articles":articles,"b":block})

def article_detail(request,article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)

    return render_to_response("article_detail.html",{'article':article})

def article_create(request,block_id):
    block_id = int(block_id)
    block = Blocks.objects.get(id=block_id)
    if request.method == 'GET':
        return render_to_response('article_create.html',{'b':block},
                context_instance = RequestContext(request))
    else:  #request.method == 'POST'
        title = request.POST['title'].strip()
        content = request.POST['content'].strip()
        if not title or not content:
            messages.add_message(request,messages.ERROR,u'标题和内容均不能为空')
            return render_to_response('article_create.html',{'b':block,'title':title,'content':content},context_instance=RequestContext(request))
        owner = User.objects.all()[0] #TODO:
        new_article = Article(block=block,owner=owner,title=title,content=content)
        new_article.save()
        messages.add_message(request,messages.INFO,u'成功发表文章')
        return redirect(reverse("article_list",args=[block.id]))