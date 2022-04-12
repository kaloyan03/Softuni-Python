from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Animal(models.Model):
    ANIMAL_NAME_MAX_LENGTH = 30
    ANIMAL_NAME_MIN_LENGTH = 2

    ANIMAL_TYPE_MAX_LENGTH = 30
    ANIMAL_TYPE_MIN_LENGTH = 2

    name = models.CharField(
        max_length=ANIMAL_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(ANIMAL_NAME_MIN_LENGTH),
        )
    )

    type = models.CharField(
        max_length=ANIMAL_TYPE_MAX_LENGTH,
        validators=[
            MinLengthValidator(ANIMAL_TYPE_MIN_LENGTH),
        ]

    )