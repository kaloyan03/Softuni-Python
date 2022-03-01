from django.urls import path

from todos.todo.views import ListTodos, CreateTodo

urlpatterns = (
    path('', ListTodos.as_view(), name='list todos'),
    path('create/', CreateTodo.as_view(), name='create todo'),
)