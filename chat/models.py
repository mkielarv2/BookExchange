from django.db import models
from django.contrib.auth import models as auth
from rest_framework import serializers

from offers.models import Offers


class Messages(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    sender = models.ForeignKey(auth.User, on_delete=models.CASCADE)
    message = models.TextField(null=False)
    sending_time = models.DateTimeField(null=False)


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
