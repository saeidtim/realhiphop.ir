from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.CustomUser)
class AdminUser(admin.ModelAdmin):
    pass
