from django import forms

from todos_list_demo.core.forms import BootstrapFormMixin
from todos_list_demo.profiles.models import Profile


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']