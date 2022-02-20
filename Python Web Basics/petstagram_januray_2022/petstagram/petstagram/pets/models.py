from django.db import models

# Create your models here.
from petstagram.profiles.models import Profile


class Pet(models.Model):
    PET_MAX_LENGTH = 30

    TYPE_CAT = 'Cat'
    TYPE_DOG = 'Dog'
    TYPE_BUNNY = 'Bunny'
    TYPE_PARROT = 'Parrot'
    TYPE_FISH = 'Fish'
    TYPE_OTHER = 'Other'

    TYPE_CHOICES = [(x,x) for x in (TYPE_CAT, TYPE_DOG, TYPE_BUNNY, TYPE_PARROT, TYPE_FISH, TYPE_OTHER)]

    name = models.CharField(
        max_length=PET_MAX_LENGTH,
        unique=True,
    )

    type = models.CharField(
        choices=TYPE_CHOICES,
        max_length=max(len(x) for x,_ in TYPE_CHOICES)
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
    )

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )