
from django.urls import path
from .views import chess_list, dungeon_zane

urlpatterns = [
    path('', chess_list, name='chess_list'),
    path('bases/', chess_list, name='bases'),
    path('base/', dungeon_zane, name='dungeon_zane'),
]