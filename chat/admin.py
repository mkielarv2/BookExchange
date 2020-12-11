from django.contrib import admin

from chat.models import Comment, Messages

admin.site.register(Comment)
admin.site.register(Messages)
