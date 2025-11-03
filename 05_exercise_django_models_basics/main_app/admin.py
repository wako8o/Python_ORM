from django.contrib import admin
from .models import Person, Blog, WeatherForecast, UserProfile, Book


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('post', 'author')

@admin.register(WeatherForecast)
class WeatherForecastAdmin(admin.ModelAdmin):
    list_display = ('date', 'temperature', 'humidity', 'precipitation')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass