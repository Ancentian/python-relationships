from django.contrib import admin

# Register your models here.
from .models import Employee, Department

admin.site.register(Department)
admin.site.register(Employee)
