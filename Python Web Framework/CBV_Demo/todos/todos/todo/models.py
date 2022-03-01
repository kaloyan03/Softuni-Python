from django.db import models

# Create your models here.


class Todo(models.Model):
    TITLE_MAX_LENGTH = 30
    DESCRIPTION_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    description = models.CharField(
        max_length=DESCRIPTION_MAX_LENGTH,
    )

    def __str__(self):
        return f"{self.title}"