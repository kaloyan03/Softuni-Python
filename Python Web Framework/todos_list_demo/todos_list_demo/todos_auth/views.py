from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from todos_list_demo.core.forms import BootstrapFormMixin
from todos_list_demo.todos_auth.forms import SignInForm, SignUpForm


def register(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)

        if user_form.is_valid():
            user_form.save()

            return redirect('login')

    else:
        user_form = SignUpForm()

    context = {
        'user_form': user_form,
    }

    return render(request, 'auth/register.html', context)



def todos_login(request):
    if request.method == 'POST':
        user_form = SignInForm(request.POST)

        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']

            user = authenticate(
                username=username,
                password=password,
            )

            if user:
                # i don't know if there should be written user_form.save() ?!
                login(request, user)
                return redirect('list todos')

    else:
        user_form = SignInForm()
    context = {
        'user_form': user_form,
    }

    return render(request, 'auth/login.html', context)


def todos_logout(request):
    logout(request)
    return redirect('login')