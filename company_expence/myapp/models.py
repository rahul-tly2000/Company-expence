from time import strftime
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    employee_code = models.CharField(max_length=20, unique=True)
    def __str__(self) -> str:
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    vendor_code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

class Expense(models.Model):
    employee_code = models.ForeignKey(Employee, on_delete=models.CASCADE)
    vendor_code = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    expense_comment = models.CharField(max_length=100)
    expense_done_on = models.DateField()
    expense_amount = models.IntegerField()

