from django.contrib import admin

from .models import Offers, Category, BookCondition, Localization, ImageURL

admin.site.register(Offers)
admin.site.register(Category)
admin.site.register(BookCondition)
admin.site.register(Localization)
admin.site.register(ImageURL)
