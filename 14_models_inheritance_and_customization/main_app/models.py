from django.db import models
from main_app.choices import ZooKeeperChoices

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

class Mammal(Animal):
    fur_color = models.CharField(max_length=50)

class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)

class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

class ZooKeeper(Employee):
    specialty = models.CharField(max_length=10, choices=ZooKeeperChoices.choices)
    managed_animals = models.ManyToManyField(Animal)

class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)
