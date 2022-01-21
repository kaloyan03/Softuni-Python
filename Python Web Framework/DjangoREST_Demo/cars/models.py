from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    mileage = models.IntegerField(null=False, default=0)
