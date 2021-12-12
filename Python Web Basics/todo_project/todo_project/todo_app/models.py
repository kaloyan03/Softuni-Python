from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name_plural = 'people'


class Todo(models.Model):
    title = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=100, null=True)
    is_done = models.BooleanField(default=False)
    owner = models.ForeignKey(Person, models.CASCADE, null=True)
