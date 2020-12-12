from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework import serializers
from django.db import models


class UserSerializer(serializers.ModelSerializer):
    user_rating = serializers.SerializerMethodField('get_rating')

    def get_rating(self, data):
        rate = Rating.objects.filter(user=data.id).aggregate(Avg('rating'))
        return rate['rating__avg']

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_rating')


class UserDeserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')


class Rating(models.Model):
    rated_user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_author')
    rating = models.IntegerField()


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class RatingDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('rating', 'rated_user')
