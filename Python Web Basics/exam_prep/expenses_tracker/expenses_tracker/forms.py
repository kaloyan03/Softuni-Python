from django import forms

from expenses_tracker.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    profile_image = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class':'form-file',
            }
        )
    )
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')


class EditProfileForm(forms.ModelForm):
    profile_image = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class':'form-file',
            }
        )
    )
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
