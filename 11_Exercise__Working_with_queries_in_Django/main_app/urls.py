
from django.urls import path
from .views import chess_list

urlpatterns = [
    path('', chess_list, name='chess_list'),
    path('bases/', chess_list, name='bases'),
]