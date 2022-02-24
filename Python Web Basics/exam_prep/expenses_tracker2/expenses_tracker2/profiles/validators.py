from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        pass

    def get_error_message(self):
        return f"Max file size is {self.max_size} MB"


def validate_only_letters(value):
    if not value.is_alpha():
        raise ValidationError('Ensure this value contains only letters.')