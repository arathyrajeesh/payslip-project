from django import forms
from .models import Employee,Salary

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'designation', 'basic_salary']

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['hra', 'da', 'allowances', 'deductions', 'leaves_taken']
