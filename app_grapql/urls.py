from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="index"),   
    path('activate/<str:token>/', views.activate, name='urltoken'),
    path('password-reset/<str:token>/', views.resetPass, name='urltoken'),
]
