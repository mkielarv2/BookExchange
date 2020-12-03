from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('<int:offer_id>/', views.MessagesView.as_view(), name='chat'),
    path('<int:offer_id>/<int:sender_id>', views.MessagesView.as_view(), name='chat_author'),
    path('getChats/<int:offer_id>', views.get_chat_view, name='get_chats'),
]