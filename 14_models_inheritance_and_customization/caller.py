import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Animal, Mammal, Bird, Reptile, ZooKeeper, Veterinarian, ZooDisplayAnimal


def create_db():
    all_animals_info = ZooDisplayAnimal.objects.all()
    for a in all_animals_info:
        print(a.display_info())
        print(a.is_endangered())
create_db()

