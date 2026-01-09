from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee,Salary
from .forms import EmployeeForm,SalaryForm

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})


def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'form': form})


def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')


def payslip_view(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)

    salary, created = Salary.objects.get_or_create(
        employee=employee,
        defaults={
            'hra': 0,
            'da': 0,
            'allowances': 0,
            'deductions': 0,
            'leaves_taken': 0,
        }
    )

    context = {
        'employee': employee,
        'salary': salary,
        'gross_salary': salary.gross_salary(),
        'net_salary': salary.net_salary(),
    }
    return render(request, 'payslip.html', context)


def salary_add_update(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)

    salary, created = Salary.objects.get_or_create(employee=employee)

    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('payslip', emp_id=employee.emp_id)
    else:
        form = SalaryForm(instance=salary)

    return render(request, 'salary_form.html', {
        'form': form,
        'employee': employee
    })
