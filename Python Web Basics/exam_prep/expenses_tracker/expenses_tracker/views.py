from django.shortcuts import render

from expenses_tracker.expenses.models import Expense
from expenses_tracker.forms import CreateProfileForm
from expenses_tracker.profiles.views import get_profile

def home_page(request):
    expenses = Expense.objects.all()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'home-with-profile.html', {'has_profile': True, 'expenses': expenses})
    else:
        profile = get_profile()

        if profile:
            budget_left = profile.budget - sum([expense.price for expense in expenses])
            return render(request, 'home-with-profile.html', {'has_profile': True, 'expenses': expenses, 'profile': profile, 'budget_left': budget_left})
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)