from django.contrib import admin
from .models import *


@admin.register(Participant)
class AdminParticipant(admin.ModelAdmin):
    pass


@admin.register(Judge)
class AdminJudge(admin.ModelAdmin):
    pass
