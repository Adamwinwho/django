#coding:utf-8
from django.shortcuts import render_to_response,redirect
import datetime
import uuid

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext
from models import ActivateCode

# Create your views here.

def register(request):
    error = ''
    if request.method == 'GET':
        return render_to_response('usercenter_register.html',{},context_instance=RequestContext(request))
    else:
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        re_password = request.POST['re_password'].strip()

        if not username or not email or not password or not re_password:
            error = u"任何字段均不能为空"
        if password != re_password:
            error = u'两次密码不一致'
        if User.objects.filter(username=username).count() > 0:
            error = u"用户名已存在"
        if User.objects.filter(email=email).count() > 0:
            error = u"该邮箱已被注册"

        if not error:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.is_active = False
            user.save()

            #获取32位随机码
            new_code = str(uuid.uuid4()).replace('-','')
            #设置过期时间
            expire_time = datetime.datetime.now()+datetime.timedelta(days=1)
            code_record = ActivateCode(owner=user,code=new_code,expire_timestamp=expire_time)
            code_record.save()
            activate_link = "http://%s%s" % (request.get_host(),reverse('usercenter_activate',args=[new_code]))
            send_mail(u'[Python部落论坛]激活邮件',u'您的激活链接为：%s' % activate_link,'1137048513@qq.com',[email],fail_silently=False)
        else:
            return render_to_response('usercenter_register.html',{'errors':error},context_instance = RequestContext(request))
        return redirect(reverse('login'))

def activate(request,code):
    query = ActivateCode.objects.filter(code=code,expire_timestamp__gte=datetime.datetime.now())
    if query.count() > 0:
        code_record = query[0]
        code_record.owner.is_active = True
        code_record.owner.save()
        return HttpResponse(u'激活成功')
    else:
        return HttpResponse(u'激活失败')
