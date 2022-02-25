from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker2.expenses.models import Expense
from expenses_tracker2.profiles.forms import EditProfileForm
from expenses_tracker2.profiles.models import Profile


def get_profile():
    profiles = Profile.objects.all()

    if profiles:
        return profiles[0]
    return None


def show_profile(request):
    profile = get_profile()
    expenses_bought = Expense.objects.count()

    context = {
        'profile': profile,
        'expenses_bought': expenses_bought,
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    if request.method == 'POST':
        profile = get_profile()
        expenses = Expense.objects.all()

        profile.delete()
        [e.delete() for e in expenses]

        return redirect('index')

    else:
        return render(request, 'profile-delete.html')

