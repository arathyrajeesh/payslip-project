from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.employee_create, name='employee_create'),
    path('edit/<int:id>/', views.employee_update, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('salary/<str:emp_id>/', views.salary_add_update, name='salary_add'),
    path('payslip/<str:emp_id>/', views.payslip_view, name='payslip'),

]
