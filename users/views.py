from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework import exceptions

from users.serializers import UserRegSerializer, UserSerializer
from .models import User
from .utils import access_token_generator, refresh_token_generator


# register user endpoint
@api_view(['POST'])
def register_user(request):
    serializer = UserRegSerializer(data=request.data, many=False)

    if serializer.is_valid():
        serializer.save()
        print(connection.queries)
        return Response(status=HTTP_201_CREATED)

    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# user login endpoint
@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    phone_number = request.data['phone_number']
    password = request.data['password']

    # creating response object
    response = Response()

    # checking login credentials
    if (phone_number is None) or (password is None):
        raise exceptions.AuthenticationFailed('Invalid credentials')

    user = User.objects.raw(f'SELECT * FROM `users_user` WHERE phone_number={phone_number}')[0]

    if (user is None):
        raise exceptions.AuthenticationFailed('User not found')

    print(user.password)

    if (not password==user.password):
        raise exceptions.AuthenticationFailed('Invalid credentials')

    user_data = UserSerializer(user).data

    access_token = access_token_generator(user)
    refresh_token = refresh_token_generator(user)

    # preparing the response
    response.set_cookie(key="refresh_token",
                        value=refresh_token, httponly=True, max_age=604800)
    response.data = {
        'access_token': access_token,
        'user': user_data
    }

    return response


# get all users endpoint
@api_view(['GET'])
def get_users(request):
    raw_users = User.objects.raw('SELECT * FROM `users_user` WHERE 1')
    users = UserSerializer(raw_users, many=True).data

    return Response(users, status=HTTP_200_OK)
