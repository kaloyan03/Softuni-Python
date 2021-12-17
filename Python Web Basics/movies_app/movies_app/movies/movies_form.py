from django import forms


class CreateMovieForm(forms.Form):
    title = forms.CharField(
        max_length=30
    )

    description = forms.CharField(
        widget=forms.TextInput
    )

    image_url = forms.URLField()