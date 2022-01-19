from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from todos_list_demo.core.forms import BootstrapFormMixin

UserModel = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'age')



class SignInForm(BootstrapFormMixin, forms.Form):
    email = forms.CharField(
        max_length=30,
    )

    password = forms.CharField(
        max_length=30,
        widget= forms.PasswordInput(),
    )


