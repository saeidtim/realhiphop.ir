from django.db import models
from profiles.models import *


class Event(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.TextField(max_length=500)
    list_participant = models.ManyToManyField(Participant, related_name='list_participant')
    list_judge = models.ManyToManyField(Judge, related_name='Judges')

    def __str__(self):
        return self.name
