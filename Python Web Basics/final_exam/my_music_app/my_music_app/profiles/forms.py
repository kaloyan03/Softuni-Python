from django import forms

from my_music_app.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    age = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder':'Age'})
    )

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')