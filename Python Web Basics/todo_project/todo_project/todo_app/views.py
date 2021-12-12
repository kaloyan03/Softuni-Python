from django.shortcuts import render, redirect
from todo_project.todo_app.models import Todo, Person
# Create your views here.

def index(request):
    context = {
        'todos' : Todo.objects.all(),
    }


    return render(request, 'index.html', context)


def create_todo(request):
    title = request.POST['title']
    description = request.POST['description']
    owner = None
    owner_name = request.POST['owner']

    owner = Person.objects\
        .filter(name=owner_name)\
        .first()


    if not owner:
        owner = Person(
            name=owner_name
        )

    owner.save()

    todo = Todo(
        title=title,
        description=description,
        owner=owner,
    )

    todo.save()

    return redirect('/')

