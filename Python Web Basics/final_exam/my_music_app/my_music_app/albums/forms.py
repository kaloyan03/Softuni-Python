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
        required=False,
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

class EditAlbumForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Album Name'}),
        label='Album Name',
    )

    artist = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Artist'}),
    )

    description = forms.CharField(
        required=False,
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

class DeleteAlbumForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disalbed'


    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image_url', 'price')