from rest_framework.urls import path

from .views import create_service, get_services, update_service, delete_service, create_subscription, get_subscriptions, \
    update_subscription

urlpatterns = [
    path('create', create_service, name='create_service'),
    path('get', get_services, name='get_services'),
    path('update/<int:pk>', update_service, name='update_service'),
    path('delete/<int:pk>', delete_service, name='delete_service'),
    path('sub/create', create_subscription, name='create_subscription'),
    path('sub/get', get_subscriptions, name='get_subscriptions'),
    path('sub/update/<int:pk>', update_subscription, name='update_subscription'),
]
