from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from petstagram.profiles.validators import validate_only_letters


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    GENDER_MAX_LENTGH = 10


    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDER_CHOICES = [(x,x) for x in (MALE, FEMALE,DO_NOT_SHOW)]

    # GENDER_CHOICES = [
    #     (MALE, 'male'),
    #     (FEMALE, 'female'),
    #     (DO_NOT_SHOW, 'do_not_show'),
    # ]

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

    profile_picture = models.URLField(

    )

    birth_date = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=max(len(x) for x, _ in GENDER_CHOICES),
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # gender = models.Choices(
    #     choices=GENDER_CHOICES,
    # )