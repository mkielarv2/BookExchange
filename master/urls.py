from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.static.register, name='register'),
    path('login/', views.static.login, name='login'),
    path('logout/', views.static.logout, name='logout'),
    path('change/', views.static.change, name='change'),
    path('create/', views.static.create, name='create'),

    path('api/register/', views.Register.as_view(), name='apiRegister'),
    path('api/login/', views.Login.as_view(), name='apiLogin'),
    path('api/logout/', views.Logout.as_view(), name='apiLogout'),
    path('api/change/', views.Change.as_view(), name='apiChange'),
    path('api/edit', views.edit_user, name='apiEditUser'),
    path('api/user/<int:user_id>', views.get_user, name='apiGetUser'),
    path('api/user/rate', views.rate, name='apiRateUser'),
    path('api/user/rating/<int:user_id>', views.delete_rate, name='apiDeleteRating'),

    path('openapi/', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),

    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
