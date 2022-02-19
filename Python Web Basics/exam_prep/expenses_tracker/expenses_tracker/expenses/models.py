from django.db import models

# Create your models here.

class Expense(models.Model):
    TITLE__MAX_LENGTH_VALUE = 30

    title = models.CharField(
        max_length=TITLE__MAX_LENGTH_VALUE
    )

    expense_image = models.URLField(

    )

    description = models.TextField(
        null=True,
    )

    price = models.FloatField(

    )



