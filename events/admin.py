from django.contrib import admin
from .models import *


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    pass