from django.contrib import admin
from .models import Employee
# Register your models here.
@admin.register(Employee)
class calendarModuleAdmin(admin.ModelAdmin):
    pass
