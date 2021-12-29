from rest_framework.urls import path

from .views import create_bill, get_bills, get_bill, update_bill, create_payment, get_payments, get_payment

urlpatterns = [
    path('create', create_bill, name='create_bill'),
    path('get', get_bills, name='get_bills'),
    path('get/<int:pk>', get_bill, name='get_bill'),
    path('update/<int:pk>', update_bill, name='update_bill'),
    path('payments/create', create_payment, name='create_payment'),
    path('payments/get', get_payments, name='get_payments'),
    path('payments/get/<int:pk>', get_payment, name='get_payment'),
]
