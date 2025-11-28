from django.contrib import admin

from main_app.models import HotelRoom


# Register your models here.

@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'amenities','price_per_night')
