# from django.shortcuts import render
#
# def index(request):
#     return render(request, 'drawing_app/index.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('drawing_board', room_name="default")
        else:
            return render(request, 'drawing_app/login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'drawing_app/login.html')

@login_required
def drawing_board(request, room_name):
    return render(request, 'drawing_app/drawing_board.html', {'room_name': room_name})