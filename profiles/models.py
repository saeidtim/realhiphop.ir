from django.db import models
from accounts.models import CustomUser
from django.contrib.auth import get_user_model

class Participant(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    rank = models.PositiveIntegerField(default=0)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Judge(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
