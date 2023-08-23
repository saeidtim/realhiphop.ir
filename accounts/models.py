from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    type = models.CharField(max_length=50, default='BreakDance')
    nickname = models.CharField(max_length=50, blank=True, null=True)
    balance = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)
    avatar = models.ImageField(upload_to='user/avatars/', blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username