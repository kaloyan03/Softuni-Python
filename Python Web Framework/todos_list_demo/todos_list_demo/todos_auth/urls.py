from django.contrib import admin
from django.urls import path
from todos_list_demo.todos_auth import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.todos_login, name='login'),
    path('logout/', views.todos_logout, name='logout')
]

import todos_list_demo.todos_auth.signals