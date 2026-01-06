import os
import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_skeleton.settings')
django.setup()

from main_app.models import Student, CreditCard

