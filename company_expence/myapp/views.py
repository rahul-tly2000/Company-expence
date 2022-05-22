from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from .models import Employee, Vendor, Expense
from .serializers import EmployeeSerializer, VendorSerializer, ExpenseSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            resp = {
                'message': 'employee created.'
            }
            return JsonResponse(resp)


def get_employee(request):
    employee_code = request.GET.get('employee_code')
    try:
        employees = Employee.objects.get(employee_code=employee_code)
    except employees.DoesNotExist:
        return HttpResponse(status=400)
    if request.method == 'GET':
        serializer = EmployeeSerializer(employees)
        resp = {
            "name": serializer.data['name'],
            "Employee_code": serializer.data['employee_code']
        }
        return JsonResponse(resp)
    

@csrf_exempt
def add_vendor(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            resp = {
                'message': 'vendor created.'
            }
            return JsonResponse(resp)


def get_vendor(request):
    vendor_code = request.GET.get('vendor_code')
    try:
        vendors = Vendor.objects.get(vendor_code=vendor_code)
    except vendors.DoesNotExist:
        return HttpResponse(status=400)
    if request.method == 'GET':
        serializer = VendorSerializer(vendors)
        resp = {
            "name": serializer.data['name'],
            "vendor_code": serializer.data['vendor_code']
        }
        return JsonResponse(resp)   


@csrf_exempt
def add_expense(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            resp = {
                'message': 'expense created.'
            }
            return JsonResponse(resp)


def get_expence_for_vendor(request):
    vendor_code = request.GET.get('vendor_code')
    id = Vendor.objects.filter(vendor_code=vendor_code)[0].id
    name = Vendor.objects.filter(vendor_code=vendor_code)[0].name
    try:
        expense = Expense.objects.filter(vendor_code=id).all()
    except expense.DoesNotExist:
        return HttpResponse(status=400)
    if request.method == 'GET':
        serializer = ExpenseSerializer(expense, many=True)
        data_list = []
        for data in serializer.data:
            emp_name = Employee.objects.filter(id = data['employee_code'])[0].name
            emp ={}
            emp["employee"] =  emp_name
            emp["expense_made_on"]= data['expense_done_on']
            emp["expense_comment"]= data['expense_comment']
            emp["expense_amount"] = data['expense_amount']
            data_list.append(emp)
        resp = {
            "name": name,
            "expenses" : data_list,
        }
        return JsonResponse(resp, safe=False) 


def get_expence_for_employee(request):
    employee_code = request.GET.get('employee_code')
    id = Employee.objects.filter(employee_code=employee_code)[0].id
    name = Employee.objects.filter(employee_code=employee_code)[0].name
    try:
        expense = Expense.objects.filter(employee_code=id).all()
    except expense.DoesNotExist:
        return HttpResponse(status=400)
    if request.method == 'GET':
        serializer = ExpenseSerializer(expense, many=True)
        data_list = []
        for data in serializer.data:
            emp_name = Vendor.objects.filter(id = data['vendor_code'])[0].name
            emp ={}
            emp["vendor"] =  emp_name
            emp["expense_made_on"]= data['expense_done_on']
            emp["expense_comment"]= data['expense_comment']
            emp["expense_amount"] = data['expense_amount']
            data_list.append(emp)
        resp = {
            "name": name,
            "expenses" : data_list,
        }
        return JsonResponse(resp, safe=False)