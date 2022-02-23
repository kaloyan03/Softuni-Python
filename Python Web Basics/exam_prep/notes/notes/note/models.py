from django.db import models

# Create your models here.

class Note(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    image_url = models.URLField(

    )

    content = models.TextField(

    )