from django.shortcuts import render, get_object_or_404
from .models import Employee, Salary

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def generate_payslip(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    salary = get_object_or_404(Salary, employee=employee)

    context = {
        'employee': employee,
        'salary': salary,
        'gross_salary': salary.gross_salary(),
        'net_salary': salary.net_salary()
    }
    return render(request, 'payslip.html', context)
