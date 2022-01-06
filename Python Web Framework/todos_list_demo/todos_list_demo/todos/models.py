from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(
        max_length=30
    )

    description = models.CharField(
        max_length=100,
    )

    is_completed = models.BooleanField(default=False)