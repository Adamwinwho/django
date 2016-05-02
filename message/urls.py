from django.conf.urls import url

urlpatterns = [
    url(r'read/(?P<message_id>\d+)$',"message.views.read_message",name="read_message"),
    url(r'list/$',"message.views.message_list",name="message_list")
]
