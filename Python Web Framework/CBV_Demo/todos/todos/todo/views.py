from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from todos.todo.models import Todo


class ListTodos(ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'list_todos.html'



class CreateTodo(CreateView):
    model = Todo
    template_name = 'create_todo.html'
    success_url = reverse_lazy('list todos')
    fields = '__all__'



