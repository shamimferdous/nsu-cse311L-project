from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nid', 'phone_number', 'role', 'name', 'email', 'area', 'road_no', 'house', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(
                validated_data['nid'], validated_data['phone_number'], validated_data['role'], validated_data['name'],
                validated_data['password'])

            return user
