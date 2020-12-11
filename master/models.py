from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class Rating(models.Model):
    rated_user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_author')
    rating = models.IntegerField()
