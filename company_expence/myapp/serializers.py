from pyexpat import model
from django.conf import settings
from rest_framework import serializers
from myapp.models import Employee, Vendor, Expense

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    expense_done_on = serializers.DateField(format='%d-%b-%Y', input_formats=['%d-%b-%Y'])
    class Meta:
        model = Expense
        fields = '__all__'