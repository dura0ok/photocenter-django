from django.contrib.auth.models import AbstractUser
from django.db import models
from entities.models import Outlet


class CustomUser(AbstractUser):
    outlet = models.ForeignKey(
        Outlet,
        on_delete=models.CASCADE,
        related_name='users',
        null=True,
        blank=True
    )