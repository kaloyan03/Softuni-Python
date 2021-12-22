from django import forms

from petstagram.core.forms import BootstrapFormMixin
from petstagram.pets.models import Pet, Comment


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class EditPetForm(CreatePetForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            )
        }


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget= forms.Textarea(
            attrs= {
                'class': 'form-control rounded-2',
            }
        )
    )
    class Meta:
        model= Comment
        fields = ['comment']