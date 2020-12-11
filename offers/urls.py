from django.urls import path

from . import views

app_name = 'offers'

urlpatterns = [
    path('categories', views.get_categories, name='get_categories'),
    path('localizations', views.get_localizations, name='get_localizations'),
    path('conditions', views.get_conditions, name='get_conditions'),
]
