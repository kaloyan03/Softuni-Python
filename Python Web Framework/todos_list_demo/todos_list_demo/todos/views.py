from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def list_todos(request):
    return render(request, 'todos/list_todos.html')


def my_profile(request, pk):
    user = User.objects.get(pk=pk)

    context = {
        'user': user
    }

    return render(request, 'my_profile.html', context)


def index(request):
    return redirect('list todos')