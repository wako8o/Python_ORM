import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Animal, Mammal, Bird, Reptile, ZooKeeper, Veterinarian, ZooDisplayAnimal


def create_db():
    is_proxy = ZooDisplayAnimal._meta.proxy

    if is_proxy:
        print("ZooDisplayAnimal is a proxy model.")
    else:
        print("ZooDisplayAnimal is not a proxy model.")
create_db()

