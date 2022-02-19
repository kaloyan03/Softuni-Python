from django.shortcuts import render, redirect

from expenses_tracker.expenses.models import Expense
from expenses_tracker.forms import EditProfileForm
from expenses_tracker.profiles.models import Profile


def get_profile():
    profiles = Profile.objects.all()

    if profiles:
        return profiles[0]
    return None

# Create your views here.
def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()

    context = {
        'profile': profile,
        'expenses_bought': len(expenses),
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('show profile')

    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        profile.delete()
        expenses = Expense.objects.all()

        for expense in expenses:
            expense.delete()

        return redirect('home page')

    else:
        return render(request, 'profile-delete.html')


