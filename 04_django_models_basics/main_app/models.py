from datetime import date

from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length= 30)
    email_address = models.EmailField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


class Department(models.Model):

    class Choices(models.TextChoices):
        SF = "SF", "Sofia",
        PL = "PL", "Plovdiv",
        VR = "VR", "Varna",
        BS = "BS", "Burgas"

    code = models.CharField(max_length=4, primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    employees_count = models.IntegerField(default=1, verbose_name="Employees Count")
    location = models.CharField(max_length=20, choices=Choices.choices)
    last_edited_on = models.DateTimeField(auto_now=True)

class Project(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration_in_days = models.IntegerField(default=0, verbose_name="Duration in Days")
    estimated_hours = models.FloatField(default=0, verbose_name="Estimated Hours")
    start_date = models.DateField(default=date.today)
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited_on = models.DateTimeField(auto_now_add=True)
