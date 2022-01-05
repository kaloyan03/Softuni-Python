from django.contrib import admin
from django.urls import path
from todos_list_demo.todos import views

urlpatterns = [
    path('list-todos/', views.list_todos, name='list todos'),
    path('my-profile/<int:pk>', views.my_profile, name='my profile'),
    path('', views.index, name='index')

]
