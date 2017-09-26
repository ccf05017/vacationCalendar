from django.contrib import admin
from .models import AuthEmployee

# Register your models here.
@admin.register(AuthEmployee)
class authEmployeeAdmin(admin.ModelAdmin):
    pass
