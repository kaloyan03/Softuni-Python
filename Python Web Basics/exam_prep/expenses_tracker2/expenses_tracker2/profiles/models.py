from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
from expenses_tracker2.profiles.validators import MaxFileSizeMbValidator, validate_only_letters


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2
    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0
    IMAGE_MAX_SIZE_MB = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        )
    )

    profile_image = models.ImageField(
        default='static/images/user.png',
        upload_to='profile_pictures',
        validators=(
            MaxFileSizeMbValidator(IMAGE_MAX_SIZE_MB),
        )
    )