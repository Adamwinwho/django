from django.shortcuts import render_to_response
from models import Blocks

# Create your views here.

def blocks_list(request):
    blocks = Blocks.objects.all().order_by("-id")
    return render_to_response("blocks_list.html",{"blocks":blocks})
