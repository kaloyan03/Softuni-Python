from django.urls import path

from todos.todo.views import ListTodos, CreateTodo, TodoDetails, DeleteTodo, EditTodo

urlpatterns = (
    path('', ListTodos.as_view(), name='list todos'),
    path('create/', CreateTodo.as_view(), name='create todo'),
    path('details/<int:pk>', TodoDetails.as_view(), name='todo details'),
    path('delete/<int:pk>', DeleteTodo.as_view(), name='delete todo'),
    path('edit/<int:pk>', EditTodo.as_view(), name='edit todo'),
)