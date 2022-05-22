from django.urls import path
from . import views

urlpatterns = [
    path('add-employee/', views.add_employee),
    path('get-employee/', views.get_employee),
    path('add-vendor/', views.add_vendor),
    path('get-vendor/', views.get_vendor),
    path('add-expense/', views.add_expense),
    path('get-expense-for-vendor/', views.get_expence_for_vendor),
    path('get-expense-for-employee/', views.get_expence_for_employee),
]