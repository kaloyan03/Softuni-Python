from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker.expenses.forms import CreateExpenseForm, EditExpenseForm
from expenses_tracker.expenses.models import Expense


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
    }

    return render(request, 'expense-create.html', context)


def edit_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense
    }

    return render(request, 'expense-edit.html', context)

def delete_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == 'POST':
        expense.delete()
        return redirect('home page')

    context = {
        'expense': expense,
    }

    return render(request, 'expense-delete.html', context)