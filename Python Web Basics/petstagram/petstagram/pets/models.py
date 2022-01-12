from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, 'Cat'),
        (TYPE_CHOICE_PARROT, 'Parrot'),
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,

    )
    name = models.CharField(
        max_length=6
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/pets',
        blank=True,
    )


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField()