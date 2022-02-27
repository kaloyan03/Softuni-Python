from django.core.exceptions import ValidationError


USERNAME_ERROR_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'


def validate_username(value):
    if not (value.isalnum() or '_' in value):
        raise ValidationError(USERNAME_ERROR_MESSAGE)
