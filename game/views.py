from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import OnlineGames
from django.contrib.auth.decorators import login_required


def game(request):
    return render(request, 'mhome.html')

@login_required
def s(request):
    return render(request, 'social.html')

@login_required
def goto(request):
    return render(request, 'goto.html')

def nl(request):
    return render(request, 'nl.html')

@login_required
def connect4(request):
    return render(request, 'Home.html')

@login_required
def w(request):
    return render(request, 'wack.html')

def privacy(request):
    return render(request, 'Privacy Policy.html')

@login_required
def onlogin(request):
    return render(request, 'games.html')

@login_required
def rules(request):
    return render(request, 'rules.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def age(request):
    return render(request, 'age.html')

def getstarted(request):
    return render(request, 'getstarted.html')

@login_required
def how(request):
    return render(request, 'How.html')

@login_required
def twitter(request):
    return render(request, 't.html')

@login_required
def start(request):
    return render(request, 's.html')

def privacyapp(request):
    return render(request, 'Privacy Policy Android.html')

@login_required
def our(request):
    return render(request, 'ourweb.html')

def error404(request, exception):
    return render(request, '404.html')

def signupuser(request):
    users = OnlineGames.objects.all()
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('g')
            except IntegrityError:
                return render(request, 'signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('g')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')