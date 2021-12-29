from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.permissions import IsAuthenticated

from fundamentals.permissions import IsEmployee
from fundamentals.utils import generate_unique_id, query_to_dicts


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsEmployee])
def create_bill(request):
    data = request.data

    cursor = connection.cursor()

    id = generate_unique_id()
    status_id = data.get('status_id')
    deadline = data.get('deadline')
    amount = data.get('amount')
    month_id = data.get('month_id')
    user_id = data.get('user_id')
    subscription_id = data.get('subscription_id')
    cursor.execute(
        f'INSERT INTO `bills`(`id`, `status_id`, `deadline`, `month_id`, `amount`, `user_id`, `subscription_id`) VALUES ({id}, "{status_id}","{deadline}","{month_id}","{amount}", "{user_id}", "{subscription_id}")')

    return Response(status=HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEmployee])
def get_bills(request):
    bills = query_to_dicts(
        'SELECT b.id, b.deadline, b.amount, m.name, sv.name, s.date_of_subscription, u.name, u.phone_number, u.area, u.road_no, u.house, bs.state FROM bills b JOIN months m ON b.month_id=m.id JOIN subscriptions s ON b.subscription_id=s.id JOIN services sv ON s.service_id=sv.id JOIN users_user u ON b.user_id=u.id JOIN bill_statuses bs ON bs.id=b.status_id')

    return Response(bills, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEmployee])
def get_bill(request, pk):
    bill = query_to_dicts(
        f'SELECT b.id, b.deadline, b.amount, m.name, sv.name, s.date_of_subscription, u.name, u.phone_number, u.area, u.road_no, u.house, bs.state FROM bills b JOIN months m ON b.month_id=m.id JOIN subscriptions s ON b.subscription_id=s.id JOIN services sv ON s.service_id=sv.id JOIN users_user u ON b.user_id=u.id JOIN bill_statuses bs ON bs.id=b.status_id WHERE b.id={pk}')

    return Response(bill, status=HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsEmployee])
def update_bill(request, pk):
    data = request.data
    print(pk)
    cursor = connection.cursor()

    status_id = data.get('status_id')

    cursor.execute(
        f'UPDATE `bills` SET status_id="{status_id}" WHERE id={pk}')

    return Response(status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsEmployee])
def create_payment(request):
    data = request.data

    cursor = connection.cursor()

    id = generate_unique_id()
    method_id = data.get('method_id')
    reference = data.get('reference')
    date = data.get('date')
    bill_id = data.get('bill_id')

    cursor.execute(
        f'INSERT INTO `payments`(`id`, `method_id`, `reference`, `date`, `bill_id`) VALUES ({id}, "{method_id}","{reference}","{date}","{bill_id}")')

    return Response(status=HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEmployee])
def get_payments(request):
    bills = query_to_dicts(
        'SELECT p.id, p.date, p.reference, pm.name AS payment_method, b.amount, b.status_id, u.name, u.nid FROM payments p JOIN payment_methods pm ON p.method_id=pm.id JOIN bills b ON b.id=p.bill_id JOIN users_user u ON b.user_id=u.id'
    )

    return Response(bills, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEmployee])
def get_payment(request, pk):
    bill = query_to_dicts(
        f'SELECT p.id, p.date, p.reference, pm.name AS payment_method, b.amount, b.status_id, u.name, u.nid FROM payments p JOIN payment_methods pm ON p.method_id=pm.id JOIN bills b ON b.id=p.bill_id JOIN users_user u ON b.user_id=u.id WHERE p.id={pk}'
    )

    return Response(bill, status=HTTP_200_OK)
