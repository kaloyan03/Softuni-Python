from django import forms

from my_music_app.albums.models import Album


class AddAlbumForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Album Name'}),
        label='Album Name',
    )

    artist = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Artist'}),
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Description'}),

    )

    image_url = forms.URLField(
        widget=forms.TextInput(attrs={'placeholder': 'Image URL'}),
        label='Image URL',
    )

    price = forms.FloatField(
        widget=forms.NumberInput(attrs={'placeholder': 'Price'}),
    )

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image_url', 'price')