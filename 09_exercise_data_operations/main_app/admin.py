from django.contrib import admin

from main_app.models import HotelRoom, Character


# Register your models here.

@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'amenities','price_per_night')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_name', 'level', 'strength', 'dexterity', 'intelligence', 'hit_points')
