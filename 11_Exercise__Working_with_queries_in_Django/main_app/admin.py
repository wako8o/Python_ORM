from django.contrib import admin

from main_app.models import ChessPlayer


# Register your models here.

@admin.register(ChessPlayer)
class ChessPlayerAdmin(admin.ModelAdmin):
    pass