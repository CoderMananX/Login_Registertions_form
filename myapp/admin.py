from django.contrib import admin
from .models import registertable
# Register your models here.

class showtable(admin.ModelAdmin):
    list_display = ["name","email"]
admin.site.register(registertable,showtable)