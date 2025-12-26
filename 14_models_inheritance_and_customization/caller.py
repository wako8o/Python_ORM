import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Animal, Mammal, Bird, Reptile

def create_db():
    animals = Animal.objects.all()
    for a in animals:
        print(f"{a.name}: {a.species}.")

create_db()

