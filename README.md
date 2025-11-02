# Python ORM

## Зип команда за архивиране за Linux/MacOS
'''
zip -r project.zip . -x "*.idea*" -x "*.venv*" -x "*__pycache__*"
''''

## Описание
Python ORM е бърз, лек и асинхронен обектно-релационен мапър с API, вдъхновен от Django. Работи със SQLite, PostgreSQL, MySQL и други бази данни.

## Основни функции
- Асинхронни заявки
- CRUD API
- ForeignKey, ManyToMany релации
- Миграции на схемите

## Инсталация

pip install python-orm

## Начално използване

from python_orm import Model

class User(Model):

name = models.CharField(max_length= 30)

email_address = models.EmailField()

birth_date = models.DateField()

works_full_time = models.BooleanField()

created_on = models.DateTimeField(auto_now_add=True)


## Конфигуриране на връзка с база данни

DATABASES = {

    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "*****", 
        "USER": "*****",
        "PASSWORD": "*****",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

Моделите се съхраняват в папката `models/`.

## Документация
- Официална документация: docs/
- API справочник: docs/api.md
- 

