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

    def get_images(self, data):
        urls = OffersURL.objects.values_list('url_id', flat=True).filter(offer_id=data.id).select()
        images = URL.objects.values_list('image', flat=True).filter(id__in=urls)
        serializer = URLSerializer(images, many=True)
        return serializer.data

    class Meta:
        model = Offers
        fields = '__all__'


class OffersDeserializer(serializers.ModelSerializer):
    class Meta:
        models = Offers
        fields = ('category', 'title', 'author', 'description', 'condition', 'location')


class URL(models.Model):
    image = models.ImageField(upload_to=settings.IMAGE_URL)


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('image',)


class OffersURL(models.Model):
    offer_id = models.ForeignKey(Offers, on_delete=models.CASCADE)
    url_id = models.ForeignKey(URL, on_delete=models.CASCADE)

