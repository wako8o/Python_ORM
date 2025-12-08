import os
from typing import List

import django
from django.db.models import Case, When, Value, F

from main_app.cheices import LaptopOperationSystem, LaptopChoices

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ChessPlayer, Meal, Dungeon, Workout, ArtworkGallery, Laptop


def show_highest_rated_art():
    highest_rated_art = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f"{highest_rated_art.art_name} is the highest-rated art with a {highest_rated_art.rating} rating!"

def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    ArtworkGallery.objects.bulk_create([first_art,second_art,])

def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()

def show_the_most_expensive_laptop():
    most_the_expensive_laptop = Laptop.objects.order_by('-price', '-id').first()
    return f"{most_the_expensive_laptop.brand} is the most expensive laptop available for {most_the_expensive_laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=['Asus','Lenovo']).update(storage=512)

def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=['Apple', 'Dell', 'Acer']).update(memory=16)

def update_operation_systems():
    Laptop.objects.filter(brand='Asus').update(operation_system='WINDOWS')
    Laptop.objects.filter(brand='Apple').update(operation_system='MAC_OS')
    Laptop.objects.filter(brand__in=['Dell', 'Acer']).update(operation_system='LINUX')
    Laptop.objects.filter(brand='Lenovo').update(operation_system='CHROME_OS')


    # Laptop.objects.update(
    #     operation_system=Case(
    #         When(brand=LaptopChoices.ASUS, then=Value(LaptopOperationSystem.WINDOWS)),
    #         When(brand=LaptopChoices.APPLE, then=Value(LaptopOperationSystem.MAC_OS)),
    #         When(brand=LaptopChoices.LENOVO, then=Value(LaptopOperationSystem.CHROME_OS)),
    #         When(brand__in=[
    #             LaptopChoices.DELL, LaptopChoices.ACER
    #         ], then=Value(LaptopOperationSystem.LINUX)
    #         ),
    #     )
    # )

def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


