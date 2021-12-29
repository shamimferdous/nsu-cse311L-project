from django.db import models

from users.models import User


# Service model
class Service(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    billing_interval = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=2500)

    class Meta:
        db_table = 'services'


# ServiceStatus model
class ServiceStatus(models.Model):
    state = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'service_statuses'


# Subscription model
class Subscription(models.Model):
    date_of_subscription = models.DateField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.ForeignKey(ServiceStatus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subscriptions'
