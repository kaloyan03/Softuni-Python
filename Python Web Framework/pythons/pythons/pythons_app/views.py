from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView

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


class Index(ListView):
    model = Python
    context_object_name = 'pythons'
    template_name = 'index.html'


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


class CreatePython(CreateView):
    model = Python
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

