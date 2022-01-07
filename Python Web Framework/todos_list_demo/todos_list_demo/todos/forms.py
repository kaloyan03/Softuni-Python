from django import forms

from todos_list_demo.core.forms import BootstrapFormMixin
from todos_list_demo.todos.models import Todo


class CreateTodoForm(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model = Todo
        fields = ('__all__')

