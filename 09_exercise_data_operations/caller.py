import os
from decimal import Decimal
from operator import invert

import django
from django.db.models import F

from main_app.choices import CharacterTypeChoices

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


def create_pet(name, species):

    pet = Pet.objects.create(name=name, species=species)
    return f"{pet.name} is a very cute {pet.species}!"

    # pet_1 = Pet.objects.create(
    #     name = 'Buddy',
    #     species = 'Dog',
    # )
    # pet_1.save()
    #
    # pet_2 = Pet.objects.create(
    #     name='Whiskers',
    #     species='Cat',
    # )
    # pet_2.save()
    #
    # pet_3 = Pet.objects.create(
    #     name='Rocky',
    #     species='Hamster',
    # )
    # pet_3.save()
    #
    # return f"{pet_1.name} is a very cute {pet_1.species}!"

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):

    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):

    if artifact.age < 250 and artifact.is_magical:
        artifact.name = new_name
        artifact.save()

def delete_all_artifacts():

    Artifact.objects.all().delete()


def show_all_locations():

    locations = Location.objects.all().order_by('-id')

    return '\n'.join(f"{location.name} has a population of {location.population}!"
                     for location in locations)


def new_capital():

    # Location.objects.first().update(is_capital=True)

    location = Location.objects.first()
    location.is_capital = True
    location.save()

def get_capitals():

    location = Location.objects.filter(is_capital=True).values('name')
    return location


def delete_first_location():

    Location.objects.first().delete()


def apply_discount():

    cars = Car.objects.all()
    for car in cars:
        price_off = Decimal(str(sum(int(x) for x in str(car.year)) / 100))
        discount_car = car.price * price_off
        total = car.price - discount_car
        car.price_with_discount = total
        car.save()


def get_recent_cars():

    cars = Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')
    return cars

def delete_last_car():

    Car.objects.last().delete()


def show_unfinished_tasks():

    task = Task.objects.all()

    return '\n'.join(
        f"Task - {t.title} needs to be done until {t.due_date}!"
        for t in task if not t.is_finished
    )

def complete_odd_tasks():

    task = Task.objects.all()
    for t in task:
        if t.id % 2 != 0:
            t.is_finished = True
            t.save()

def encode_and_replace(text: str, task_title: str):

    task = Task.objects.all()
    encoded = ''.join(chr(ord(x) - 3) for x in text)

    for t in task :
        if t.title == task_title:
            t.description = encoded
            t.save()

def get_deluxe_rooms():

    hotel = HotelRoom.objects.all()

    rooms = []
    for x in hotel:
        if x.room_type == 'Deluxe' and x.id % 2 == 0:
            rooms.append(x)
    return '\n'.join(
        f"Deluxe room with number {x.room_number} costs {x.price_per_night}$ per night!"
        for x in rooms
        )

def increase_room_capacity():
    hotel = HotelRoom.objects.all().order_by('id')
    for index, h in enumerate(hotel):
        if h.is_reserved:
            if index == 0:
                h.capacity += h.id
            else:
                h.capacity += hotel[index - 1].capacity
            h.save()

def reserve_first_room():
    hotel = HotelRoom.objects.first()
    hotel.is_reserved = True
    hotel.save()

def delete_last_room():
    room = HotelRoom.objects.last()

    if not room.is_reserved:
        room.delete()



def update_characters():


    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4
    )

    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
        inventory='The inventory is empty'
    )

    # characters = Character.objects.all()
    # for character in characters:
    #
    #     if character.class_name == 'Mage':
    #         character.level += 3
    #         character.intelligence -= 7
    #
    #     elif character.class_name == 'Warrior':
    #         character.hit_points //= 2
    #         character.dexterity += 4
    #
    #     elif character.class_name in ['Assassin', 'Scout']:
    #         character.inventory = 'The inventory is empty'


def fuse_characters(first_character: Character, second_character: Character) -> None:

    inventory = None

    if first_character.class_name in [CharacterTypeChoices.MAGE, CharacterTypeChoices.SCOUT]:
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"

    elif first_character.class_name in [CharacterTypeChoices.WARRIOR, CharacterTypeChoices.ASSASSIN]:
        inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=first_character.name + ' ' + second_character.name,
        class_name=CharacterTypeChoices.FUSION,
        level=(first_character.level + second_character.level) // 2,
        strength=(first_character.strength + second_character.strength) * 1.2,
        dexterity=(first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=(first_character.hit_points + second_character.hit_points),
        inventory=inventory
    )

    first_character.delete()
    second_character.delete()

def grand_dexterity():
    Character.objects.update(dexterity=30)

def grand_intelligence():
    Character.objects.update(intelligence=40)

def grand_strength():
    Character.objects.update(strength=50)

def delete_characters():
    Character.objects.filter(invert='The inventory is empty').delete()
