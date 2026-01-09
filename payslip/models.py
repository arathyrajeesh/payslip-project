from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    basic_salary = models.FloatField()

    def __str__(self):
        return self.name


class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    hra = models.FloatField()
    da = models.FloatField()
    allowance = models.FloatField()
    deductions = models.FloatField()
    leaves_taken = models.IntegerField(default=0)

    def gross_salary(self):
        return self.employee.basic_salary + self.hra + self.da + self.allowance

    def net_salary(self):
        return self.gross_salary() - self.deductions
