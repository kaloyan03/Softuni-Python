from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
def index(req):
    pythons = Python.objects.all()

    context = {
        'pythons': pythons,
        'current_path': req.path,
    }

    return render(req, 'index.html', context)


def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        context = {
            'form': form,
            'current_path': req.path,
        }
        return render(req, 'create.html', context)
    else:
        form = PythonCreateForm(req.POST, req.FILES)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
