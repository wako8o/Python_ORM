from django.shortcuts import render

# Create your views here.

from main_app.models import ChessPlayer, Dungeon

def chess_list(request):
    chess = ChessPlayer.objects.all()

    return render(request, 'base/chess.html', {'chess': chess})

def dungeon_zane(request):
    zone = Dungeon.objects.all()
    return render(request, 'base/dungeon.html', {'zone': zone})