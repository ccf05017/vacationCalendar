from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AuthEmployee(models.Model):
    IDCNETWORK = 'nw'
    IDCTECHNOLOGY = 'sr'
    SYSTEMADMIN = 'sa'
    DEPARTMENT_CHOICES = (
        (IDCNETWORK, "IDC_Network"),
        (IDCTECHNOLOGY, "IDC_Technology"),
        (SYSTEMADMIN, "Administrator"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    realName = models.CharField(max_length=50)
    department = models.CharField(
        max_length = 2,
        choices = DEPARTMENT_CHOICES,
        default = IDCNETWORK,
    )

    def __str__(self):
        return self.realName
