from rest_framework.urls import path

from .views import register_user, user_login, get_users

urlpatterns = [
    path('register', register_user, name='register_user'),
    path('login', user_login, name='user_login'),
    path('', get_users, name='get_users'),
]