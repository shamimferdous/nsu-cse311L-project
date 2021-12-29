from django.db import models

from services.models import Subscription
from users.models import User


# Bill Status Model
class BillStatus(models.Model):
    state = models.CharField(max_length=50)

    class Meta:
        db_table = 'bill_statuses'


# Month Model
class Month(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'months'


# Bill model
class Bill(models.Model):
    status = models.ForeignKey(BillStatus, on_delete=models.CASCADE)
    deadline = models.DateField(null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'bills'


# PaymentMethod model
class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'payment_methods'


# Payment Model
class Payment(models.Model):
    method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    date = models.DateField(null=False, blank=False)
    reference = models.CharField(max_length=100, null=False, blank=False)
    bill = models.ForeignKey(Bill, on_delete=models.PROTECT)

    class Meta:
        db_table = 'payments'
