from django.db import models

# Create your models here.
class EmployeeManager(models.Manager):
    def create_employee(self, employeeNumber, name, department, vacationDate):
        employee = self.create(
            employeeNumber=employeeNumber,
            name=name,
            department=department,
            vacationDate=vacationDate
        )

        return employee



class Employee(models.Model):
    # team_choices
    IDCNETWORK = 'nw'
    IDCTECHNOLOGY = 'sr'
    SYSTEMADMIN = 'sa'
    DEPARTMENT_CHOICES = (
        (IDCNETWORK, "IDC_Network"),
        (IDCTECHNOLOGY, "IDC_Technology"),
        (SYSTEMADMIN, "Administrator"),
    )

    # model_attributes
    employeeNumber = models.IntegerField()
    name = models.CharField(max_length=50)
    department = models.CharField(
        max_length = 2,
        choices = DEPARTMENT_CHOICES,
        default = IDCNETWORK,
    )
    vacationDate = models.DateField()

    objects = EmployeeManager()

    def __str__(self):
        return self.name
    def as_dict(self):
        return {
            "name": self.name,
            "department": self.department,
            "employeeNumber": self.employeeNumber,
            "vacationDate": self.vacationDate.day
        }
