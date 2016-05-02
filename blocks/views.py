from django.shortcuts import render_to_response
from models import Blocks
from message.models import UserMessage
# Create your views here.

def blocks_list(request):
    if request.user.is_authenticated():
        msg_cnt = UserMessage.objects.filter(owner=request.user,status=0).count()
    else:
        msg_cnt = 0
    blocks = Blocks.objects.all().order_by("-id")
    return render_to_response("blocks_list.html",{"blocks":blocks,"user":request.user,'msg_cnt':msg_cnt})
