from django.shortcuts import render

# Create your views here.

from main_app.models import ChessPlayer

def chess_list(request):
    chess = ChessPlayer.objects.all()

    return render(request, 'base/chess.html', {'chess': chess})
