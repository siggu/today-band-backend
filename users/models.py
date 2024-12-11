from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.URLField(blank=True)
    name = models.CharField(max_length=30, default="")
