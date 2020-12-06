from django.contrib.auth import models as auth
from django.db import models
from rest_framework import serializers


class Category(models.Model):
    name = models.CharField(max_length=25)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookCondition(models.Model):
    condition = models.CharField(max_length=16)


class BookConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCondition
        fields = '__all__'


class Localization(models.Model):
    name = models.CharField(max_length=25)


class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = '__all__'


class Offers(models.Model):
    user = models.ForeignKey(auth.User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.FloatField()
    rating_count = models.IntegerField()
    condition = models.ForeignKey(BookCondition, on_delete=models.CASCADE)
    location = models.ForeignKey(Localization, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)


class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = '__all__'
