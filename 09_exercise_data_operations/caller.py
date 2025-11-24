import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact


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

    Artifact.objects.create(name=name, origin=origin, age=age, description=description, is_magical=is_magical)

    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):

    if artifact.age < 250 and artifact.is_magical:
        artifact.name = new_name
        artifact.save()

def delete_all_artifacts():

    Artifact.objects.all().delete()