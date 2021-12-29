from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.permissions import IsAuthenticated

from fundamentals.permissions import IsEmployee
from fundamentals.utils import generate_unique_id, query_to_dicts
from services.models import Service, Subscription
from services.serializers import ServiceSerializer, SubscriptionSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsEmployee])
def create_service(request):
    data = request.data

    cursor = connection.cursor()

    id = generate_unique_id()
    name = data.get('name')
    price = data.get('price')
    billing_interval = data.get('billing_interval')
    description = data.get('description')
    cursor.execute(
        f'INSERT INTO `services`(`id`, `name`, `price`, `billing_interval`, `description`) VALUES ({id}, "{name}",{price},"{billing_interval}","{description}")')

    return Response(status=HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEmployee])
def get_services(request):
    raw_services = Service.objects.raw('SELECT * FROM `services` WHERE 1')

    services = ServiceSerializer(raw_services, many=True).data

    return Response(services, status=HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsEmployee])
def update_service(request, pk):
    data = request.data
    print(pk)
    cursor = connection.cursor()

    name = data.get('name')
    price = data.get('price')
    billing_interval = data.get('billing_interval')
    description = data.get('description')
    cursor.execute(
        f'UPDATE `services` SET name="{name}",price={price},billing_interval="{billing_interval}",description="{description}" WHERE id={pk}')

    return Response(status=HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsEmployee])
def delete_service(request, pk):
    print(pk)
    cursor = connection.cursor()

    cursor.execute(
        f'DELETE FROM `services` WHERE id={pk}')

    return Response(status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsEmployee])
def create_subscription(request):
    data = request.data

    cursor = connection.cursor()

    id = generate_unique_id()
    date_of_subscription = data.get('date_of_subscription')
    status_id = data.get('status_id')
    user_id = data.get('user_id')
    service_id = data.get('service_id')

    cursor.execute(
        f'INSERT INTO `subscriptions`(`id`, `date_of_subscription`, `status_id`, `user_id`, `service_id`) VALUES ({id}, "{date_of_subscription}", "{status_id}",{user_id},"{service_id}")')

    return Response(status=HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEmployee])
def get_subscriptions(request):
    subscriptions = query_to_dicts(
        "SELECT s.id, s.user_id, s.date_of_subscription, u.nid, u.name, ss.state, sv.name, sv.price FROM subscriptions s JOIN users_user u ON s.user_id=u.id JOIN service_statuses ss ON s.status_id=ss.id JOIN services sv ON s.service_id=sv.id")
    return Response(subscriptions, status=HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsEmployee])
def update_subscription(request, pk):
    data = request.data

    cursor = connection.cursor()

    status_id = data.get('status_id')
    service_id = data.get('service_id')

    cursor.execute(
        f'UPDATE `subscriptions` SET status_id="{status_id}", service_id="{service_id}" WHERE id={pk}')

    return Response(status=HTTP_200_OK)
