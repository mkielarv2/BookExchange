from django.contrib.auth import models as auth
from django.db import models
from rest_framework import serializers


class Category(models.Model):
    name = models.CharField(max_length=25)


class Offers(models.Model):
    user = models.ForeignKey(auth.User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()


class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = '__all__'
