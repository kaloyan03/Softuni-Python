from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if value.isalpha():
        raise ValidationError('Value must contain only letters')