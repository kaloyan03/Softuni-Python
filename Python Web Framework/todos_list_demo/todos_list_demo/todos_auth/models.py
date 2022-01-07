from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Profile(models.Model):
    age = models.IntegerField(
        null=True,
        blank = True,
    )

    profession = models.CharField(
        max_length=20,
        blank=True,
    )

    location = models.CharField(
        max_length=20,
        blank = True,
    )

    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
    )