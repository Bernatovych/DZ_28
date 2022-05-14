from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from news import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pars/', views.pars, name='pars'),
]
