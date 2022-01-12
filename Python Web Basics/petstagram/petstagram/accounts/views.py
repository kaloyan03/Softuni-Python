from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from petstagram.accounts.forms import UserProfileForm, SignInForm
from petstagram.accounts.models import UserProfile


def sign_up(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)

            profile.user = user
            profile.save()



    else:
        user_form = UserCreationForm
        profile_form = UserProfileForm
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "current_path": request.path,
    }
    return render(request, 'auth/signup.html', context)


def sign_in(request):
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
                login(request, user)
                return redirect('home page')
    else:
        user_form = SignInForm

    context = {
        "user_form": user_form,
        "current_path": request.path,
    }
    return render(request, 'auth/login.html', context)


def sign_out(request):
    logout(request)
    return redirect('sign in')


def profile(request, pk):
    a = request.user
    profile = UserProfile.objects.get(user_id=request.user.id)

    context = {
        'profile': profile,
    }

    return render(request, 'auth/user_profile.html', context)