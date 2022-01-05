from django import forms

from todos_list_demo.todos_auth.models import Profile


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=30,
    )

    password = forms.CharField(
        max_length=30,
        widget= forms.PasswordInput(),
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']