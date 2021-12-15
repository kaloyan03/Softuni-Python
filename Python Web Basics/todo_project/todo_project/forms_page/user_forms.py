from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

"""
•	Name: 
	Must start with an uppercase letter and have a minimum length of 6.
	You can use a built-in validator for the minimum length.
	Validation Error message: "The name must start with an uppercase letter."
•	Age: 
	Must be bigger than or equal to 0
	You can use the built-in validator for the validation or create your own
	Validation Error message: "The age cannot be less than zero."
•	Email: 
	Contains @ and dot
	You can use the built-in validator for the validation
	Validation Error message: "Enter a valid email."
•	Password: 
	Must have a minimum length of 8 and can only contain letters and numbers.
	You can use a built-in validator for the minimum length and a custom one for the requirements
	Validation Error message: "Enter a valid password."

"""


def validate_name(value):
    # MinLengthValidator(6)(value)

    if value[0] != value[0].upper() or len(value) < 6:
        raise ValidationError('The name must start with an uppercase letter.')


def validate_age(value):
    if value < 0:
        raise ValidationError('The age cannot be less than zero.')


def validate_password(value):
    if len(value) < 8 :
        raise ValidationError('Enter a valid password.')

    if any([not x.isalnum() for x in value]):
        raise ValidationError('Enter a valid password.')



class UserForm(forms.Form):
    name = forms.CharField(
        validators=[
            validate_name,
        ]
    )
    age = forms.IntegerField(
        validators=[
            validate_age,
        ]
    )
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[
            validate_password,
        ]
    )
    text = forms.CharField(
        widget=forms.Textarea(),

    )


