from django import forms

from expenses_tracker.expenses.models import Expense


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')

class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')