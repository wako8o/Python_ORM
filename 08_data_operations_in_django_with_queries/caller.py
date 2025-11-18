import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student
# Run and print your queries
...
''
...

def add_students():
    students_1 = Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date=date(1995, 5, 15),
        email='john.doe@university.com'
    )
    students_1.save()

    students_2 = Student.objects.create(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',

        email='jane.smith@university.com'
    )
    students_2.save()

    students_3 = Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date=date(1998, 2, 10),
        email='alice.johnson@university.com'
    )
    students_3.save()

    students_4 = Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date=date(1996, 11, 25),
        email='bob.wilson@university.com'
    )
    students_4.save()


def get_students_info():
    students = Student.objects.all()
    return "\n".join(f"Student №{student.student_id}: "
                     f"{student.first_name} {student.last_name}; "
                     f"Email: {student.email}" for student in students)

def update_students_emails():
    all_students = Student.objects.all()
    domain_email = "uni-students.com"
    for student in all_students:
        student.emails = student.email.split('@')
        student.email = student.email.replace(student.email.split('@')[1], domain_email)
        print(student.email)
        student.save()

def truncate_students():
    Student.objects.all().delete()

