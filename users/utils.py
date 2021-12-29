import math

import jwt
import datetime

from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


# defining access_token_generator function
def access_token_generator(user):
    """generates and returns an access token
    Args:
        user (User): The user for which the token will be generated
    Returns:
        str: access token
    """

    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5, minutes=155),
        'iat': datetime.datetime.utcnow()
    }

    access_token = jwt.encode(payload,
                              '1234', algorithm='HS256')

    return access_token


# defining refresh_token_generator function
def refresh_token_generator(user):
    """generates and returns an refresh token
    Args:
        user (User): The user for which the token will be generated
    Returns:
        str: refresh token
    """

    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }

    refresh_token = jwt.encode(payload,
                               '1234', algorithm='HS256')

    return refresh_token


# add reward point
def add_reward_points(order_amount, user):
    reward_points = math.floor(order_amount / 50)

    user.reward_points = user.reward_points + reward_points
    user.save()


# remove reward point
def remove_reward_points(reward_points, user):
    if reward_points > user.reward_points:
        return Response('Malicious use of reward points', HTTP_400_BAD_REQUEST)

    user.reward_points = user.reward_points - reward_points
    user.save()
