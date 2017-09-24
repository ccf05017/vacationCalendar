from django.db import models

# Create your models here.
class Employee(models.Model):
    # team_choices
    IDCNETWORK = 'nw'
    IDCTECHNOLOGY = 'sr'
    DEPARTMENT_CHOICES = (
        (IDCNETWORK, "IDC_Network"),
        (IDCTECHNOLOGY, "IDC_Technology"),
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
    def __str__(self):
        return self.name
    def as_dict(self):
        return {
            "name": self.name,
            "department": self.department,
            "employeeNumber": self.employeeNumber,
            "vacationDate": self.vacationDate.day
        }
