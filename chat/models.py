from django.db import models
from django.contrib.auth import models as auth
from rest_framework import serializers

from master.models import UserSerializer
from offers.models import Offers


class Messages(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    sender = models.ForeignKey(auth.User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(auth.User, on_delete=models.CASCADE, related_name='recipient')
    message = models.TextField()
    sending_time = models.DateTimeField()


class MessagesSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Messages
        fields = '__all__'


class MessagesDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('recipient', 'offer', 'message')


class Comment(models.Model):
    user = models.ForeignKey(auth.User, on_delete=models.CASCADE)
    author = models.ForeignKey(auth.User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    adding_time = models.DateTimeField()


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'content')
