from django.urls import path
from todo_project.todo_app.views import index, create_todo

urlpatterns = [
    path('', index, name='home page'),
    path('create-todo', create_todo)
]