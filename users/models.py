from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# custom account manager
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, nid, role, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(nid, role, name, password, **other_fields)

    def create_user(self, nid, phone_number, role, name, password, **other_fields):

        if not phone_number:
            raise ValueError(_('Phone number must be provided'))

        user = self.model(nid=nid, phone_number=phone_number, role=role,
                          name=name, **other_fields)
        user.set_password(password)
        user.save()

        return user


# custom account manager
class User(AbstractBaseUser, PermissionsMixin):
    role_choices = (
        ('customer', 'Customer'),
        ('employee', 'Employee'),
    )

    nid = models.CharField(_('phone number'), max_length=10, unique=True)
    phone_number = models.CharField(unique=True, max_length=11)
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=False, null=False)
    area = models.CharField(max_length=255)
    road_no = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    role = models.CharField(
        max_length=10, choices=role_choices, default='customer')
    timestamp = models.DateTimeField(default=timezone.now)
    registration_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'nid'
    REQUIRED_FIELDS = ['role', 'name']

    def __str__(self):
        return f'{self.name}, {self.phone_number}'
