from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
from todos_list_demo.todos.forms import CreateTodoForm
from todos_list_demo.todos.models import Todo


def list_todos(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos,
    }


    return render(request, 'todos/list_todos.html', context)


def my_profile(request, pk):
    user = User.objects.get(pk=pk)

    context = {
        'user': user
    }

    return render(request, 'my_profile.html', context)


def index(request):
    return redirect('list todos')


def create_todo(request):
    if request.method == 'POST':
        form = CreateTodoForm(request.POST)

        if form.is_valid():
            form.save()
            redirect('list todos')

    else:
        form = CreateTodoForm()

    context = {
        'form': form,
    }

    return render(request, 'todos/create_todo.html', context)