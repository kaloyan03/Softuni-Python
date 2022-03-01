from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

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

class EditTodo(UpdateView):
    model = Todo
    template_name = 'edit_todo.html'
    success_url = reverse_lazy('list todos')
    fields = '__all__'




class TodoDetails(DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo_details.html'


class DeleteTodo(DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    context_object_name = 'todo'
    success_url = reverse_lazy('list todos')




