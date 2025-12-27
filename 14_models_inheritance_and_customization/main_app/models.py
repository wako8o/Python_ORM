from django.core.exceptions import ValidationError
from django.db import models
from main_app.choices import ZooKeeperChoices
from datetime import date

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    @property
    def age(self):
        today = date.today()
        age = today - self.birth_date
        return age.days // 365


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

    def clean(self):
        if self.specialty not in ZooKeeperChoices.values:
            raise ValidationError("Specialty must be a valid choice.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)


class ZooDisplayAnimal(Animal):
    def display_info(self):
        return (f"Meet {self.name}! "
                f"Species: {self.species}, "
                f"born {self.birth_date}. "
                f"It makes a noise like '{self.sound}'.")

    def is_endangered(self):
        extinct_type = ["Cross River Gorilla", "Orangutan", "Green Turtle"]
        if self.species not in extinct_type:
            return f"{self.species} is not at risk."
        return f"{self.species} is at risk!"

    class Meta:
        proxy = True