from rest_framework import serializers

from .models import Service, Subscription


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    # service = ServiceSerializer(read_only=True)


    class Meta:
        model = Subscription
        fields = '__all__'
