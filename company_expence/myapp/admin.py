import site
from django.contrib import admin
from .models import Employee, Vendor, Expense

admin.site.register(Employee)
admin.site.register(Vendor)
admin.site.register(Expense)