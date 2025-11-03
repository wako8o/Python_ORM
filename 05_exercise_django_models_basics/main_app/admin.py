from django.contrib import admin
from .models import Person, Blog


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('post', 'author')

