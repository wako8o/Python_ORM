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
- Валидация с pydantic
- ForeignKey, ManyToMany релации
- Миграции на схемите

## Инсталация

pip install python-orm

## Начално използване

from python_orm import Model, IntegerField, StringField

class User(Model):
id = IntegerField(primary_key=True)
name = StringField()
email = StringField(unique=True)
Създаване на нов запис

user = User(name="Ivan", email="ivan@example.com")
user.save()

found = User.filter(name="Ivan").first()
print(found)

## Конфигуриране

from python_orm import connect
connect(db_uri="postgres://user:pass@localhost:5432/mydb")

Моделите се съхраняват в папката `models/`.

## Документация
- Официална документация: docs/
- API справочник: docs/api.md
- 

