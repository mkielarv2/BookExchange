from django.contrib.auth import models as auth
from django.db import models
from rest_framework import serializers

from djangoBookExchange import settings
from master.models import UserSerializer


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookCondition(models.Model):
    condition = models.CharField(max_length=16)

    def __str__(self):
        return self.condition


class BookConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCondition
        fields = '__all__'


class Localization(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


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
    condition = models.ForeignKey(BookCondition, on_delete=models.CASCADE)
    location = models.ForeignKey(Localization, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class OffersSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    condition = BookConditionSerializer()
    location = LocalizationSerializer()
    images = serializers.SerializerMethodField('get_images')

    @staticmethod
    def get_images(data):
        images = ImageURL.objects.filter(offer_id=data.id)
        return [str(image) for image in images]

    class Meta:
        model = Offers
        fields = '__all__'


class OffersDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = ('category', 'title', 'author', 'description', 'condition', 'location')


class ImageURL(models.Model):
    offer_id = models.ForeignKey(Offers, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=settings.IMAGE_URL)

    def __str__(self):
        return str(self.image)
