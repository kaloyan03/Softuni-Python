from django.db import models

# Create your models here.
class Expense(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    expense_image = models.URLField(

    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField(

    )