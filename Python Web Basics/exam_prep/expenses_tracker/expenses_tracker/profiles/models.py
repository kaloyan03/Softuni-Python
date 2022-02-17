from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

# Create your models here.
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeValueValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        file_size_in_bytes = self.__megabytes_to_bytes(value)
        if file_size_in_bytes > self.max_size:
            raise ValidationError(f'{self.__get_error_message()}')

    @staticmethod
    def __megabytes_to_bytes(value):
        return  value * 1024 * 1024

    def __get_error_message(self):
        return f'Max file size is {self.max_size:.2f} MB'


VALIDATE_ONLY_LETTERS_ERROR_MESSAGE = 'Ensure this value contains only letters.'


def validate_only_letters(value):
    if not value.isdigit():
        return ValidationError(VALIDATE_ONLY_LETTERS_ERROR_MESSAGE)


class Profile(models.Model):
    FIRST_NAME_MAX_VALUE = 15
    FIRST_NAME_MIN_VALUE = 2

    LAST_NAME_MAX_VALUE = 15
    LAST_NAME_MIN_VALUE = 2

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    MAX_FILE_SIZE_VALUE = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_VALUE,
        validators=(validate_only_letters,
                    MinLengthValidator(2))
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_VALUE,
        validators=(validate_only_letters,
                    MinLengthValidator(2))

    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
                    )
    )

    profile_image = models.FileField(
        upload_to='profiles',
        validators=(
            MaxFileSizeValueValidator(MAX_FILE_SIZE_VALUE),
                    )
    )

