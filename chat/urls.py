from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('message', views.send_message, name='send_message'),
    path('getChats', views.get_chat_offers, name='get_offers'),
    path('getChats/<int:offer_id>', views.get_chat, name='get_chats'),
    path('getChats/<int:offer_id>/<int:user_id>', views.get_messages, name='get_messages'),
    path('getComments/<int:user_id>', views.get_comments, name='get_comments'),
    path('comment', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
]