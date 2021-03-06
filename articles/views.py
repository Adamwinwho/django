#coding:utf-8
from django.shortcuts import render_to_response,redirect
from blocks.models import Blocks
from models import Article
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from comment.models import Comment
from utils.paginator import paginator_queryset
# Create your views here.

#block_id是从urls.py中取得,是字符串类型
def article_list(request,block_id):
    block_id = int(block_id)
    page_no = int(request.GET.get("page_no",'1'))
    block = Blocks.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")

    #每页显示6条
    p = Paginator(articles,6)
    if page_no > p.num_pages:
        page_no = p.num_pages
    if page_no < 1:
        page_no = 1
    page_links = [i for i in range(page_no-5,page_no+6) if i>0 and i<=p.num_pages]
    page = p.page(page_no)
    previous_link = page_links[0]-1
    next_link = page_links[-1]+1

    return render_to_response("article_list.html",{"articles":page.object_list,"b":block,"has_previous":previous_link>0,"has_next":next_link<=p.num_pages,"previous_link":previous_link,"next_link":next_link,"page_cnt":p.num_pages,"current_no":page_no,"page_links":page_links},context_instance=RequestContext(request))

def article_detail(request,article_id):
    page_no = int(request.GET.get("comment_page_no","1"))
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article,status=0) 
    comments,pagination_data = paginator_queryset(comments,page_no,cnt_per_page=3)
    return render_to_response("article_detail.html",{'article':article,"comments":comments,"pagination":pagination_data},context_instance=RequestContext(request))

#发表文章前必须登陆
@login_required
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
        #owner = User.objects.all()[0] #TODO:
        new_article = Article(block=block,owner=request.user,title=title,content=content)
        new_article.save()
        messages.add_message(request,messages.INFO,u'成功发表文章')
        return redirect(reverse("article_list",args=[block.id]))
