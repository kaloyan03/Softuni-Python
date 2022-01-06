from django import forms

from todos_list_demo.todos.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('__all__')