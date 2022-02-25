from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker2.expenses.forms import CreateExpenseForm, EditExpenseForm
from expenses_tracker2.expenses.models import Expense


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

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
            return redirect('index')

    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'expense-edit.html', context)


def delete_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == 'POST':
        expense.delete()
        return redirect('index')

    else:
        context = {
            'expense': expense,
        }

        return render(request, 'expense-delete.html', context)

