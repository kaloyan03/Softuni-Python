from django import forms

from petstagram.accounts.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']


class SignInForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(
        widget=forms.PasswordInput(
        ),
    )
