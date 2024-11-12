from django.db import models
from django.utils.translation import gettext as _

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    name = models.CharField(max_length=100, verbose_name=_("Department Name"))
    description = models.TextField(blank=True, verbose_name=_("Description"))

    def __str__(self):
        return _(f"{self.first_name} {self.last_name}")

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Department Name"))
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name