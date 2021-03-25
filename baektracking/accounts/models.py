from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    baekjoon_id = models.CharField(max_length=100)
    profile_image = models.ImageField(blank=True, null=True)