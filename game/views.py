from django.shortcuts import render

def game(request):
    return render(request, 'mhome.html')

def connect4(request):
    return render(request, 'Home.html')

def tic(request):
    return render(request, 'tictac.html')

def w(request):
    return render(request, 'wack.html')

def privacy(request):
    return render(request, 'Privacy Policy.html')


def rules(request):
    return render(request, 'rules.html')


def about(request):
    return render(request, 'about.html')

def age(request):
    return render(request, 'age.html')


def error404(request, exception):
    return render(request, '404.html')

def how(request):
    return render(request, 'How.html')

def twitter(request):
    return render(request, 'Twitter.html')

def privacyapp(request):
    return render(request, 'Privacy Policy Android.html')