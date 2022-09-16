from unicodedata import name
import django
from django.urls import URLPattern, path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]