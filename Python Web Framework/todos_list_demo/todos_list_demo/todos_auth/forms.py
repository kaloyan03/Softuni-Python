from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from todos_list_demo.core.forms import BootstrapFormMixin
from todos_list_demo.todos_auth.models import Profile

class SignUpForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class SignInForm(BootstrapFormMixin, forms.Form):
    username = forms.CharField(
        max_length=30,
    )

    password = forms.CharField(
        max_length=30,
        widget= forms.PasswordInput(),
    )


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']