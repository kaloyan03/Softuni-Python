from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker2.expenses.models import Expense
from expenses_tracker2.profiles.forms import CreateProfileForm
from expenses_tracker2.profiles.views import get_profile


def index(request):
    profile = get_profile()
    expenses = Expense.objects.all()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:

        form = CreateProfileForm()

    context = {
        'form': form,
        'expenses': expenses,
        'profile': profile,
    }

    if profile:
        total_expenses_price = sum([x.price for x in expenses])
        budget_left = total_expenses_price - profile.budget
        context['budget_left'] = budget_left

        return render(request, 'home-with-profile.html', context)

    return render(request, 'home-no-profile.html', context)

