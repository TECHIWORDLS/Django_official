from django.contrib import admin
from django.urls import path

from todo_app import views

urlpatterns = [
    path('', views.home),
    path('home_confirm', views.home_confrim),
]
