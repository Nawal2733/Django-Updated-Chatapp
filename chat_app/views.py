from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreateForm

# Create your views here.
@login_required(login_url='/sign_in')
def index(request):
    return render(request, 'chat/index.html', {})


@login_required(login_url='/sign_in')
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username' : mark_safe(json.dumps(request.user.username))
    })


def sing_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/chat/test')
    else:        
        form = AuthenticationForm()
        return render(request, 'auth/sign_in.html',{'form': form})


def sing_up(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/chat/test')
        else:
            print("sommething Error")
    form = UserCreateForm()
    return render(request, 'auth/sign_up.html',{'form': form})

def log_out(request):
    logout(request)
    return redirect('/sign_in')