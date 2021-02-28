"""connect4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from game import views
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'game.views.error404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.game, name='home'),
    path('connect4/', views.connect4, name='game4'),
    path('tictactoe/', views.tic, name='tic'),
    path('tennisgame/', views.tennis, name='chess'),
    path('privacypolicy/', views.privacy, name='privacy'),
    path('rules/', views.rules, name='rules'),
    path('about/', views.about, name='about'),
    path('age/', views.age, name='age'),
    path('howtoplay/', views.how, name='how'),
    path('tweets/', views.twitter, name='tweets'),
    path('privacypolicyandroid/', views.privacyapp, name='app'),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)