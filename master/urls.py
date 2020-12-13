from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.static.register, name='register'),
    path('login/', views.static.login, name='login'),
    path('logout/', views.static.logout, name='logout'),
    path('change/', views.static.change, name='change'),

    path('api/register/', views.Register.as_view(), name='apiRegister'),
    path('api/login/', views.Login.as_view(), name='apiLogin'),
    path('api/logout/', views.Logout.as_view(), name='apiLogout'),
    path('api/change/', views.Change.as_view(), name='apiChange'),
    path('api/edit', views.edit_user, name='apiEditUser'),
    path('api/user/<int:user_id>', views.get_user, name='apiGetUser'),
    path('api/user/rate', views.rate, name='apiRateUser'),
    path('api/user/rating/<int:user_id>', views.delete_rate, name='apiDeleteRating'),

    # path('registerTab/', views.static.registerTab, name='registerTab'),
    # path('loginTab/', views.static.registerTab, name='loginTab'),
    # path('productTab/', views.static.productTab, name='productTab'),
    # path('shopTab/', views.static.shopTab, name='shopTab'),
    # path('sorting/', views.static.sorting, name='sorting'),
    # path('userProducts/', views.static.userProducts, name='userProducts'),

]
