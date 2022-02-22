from django.contrib import admin

# Register your models here.
from petstagram.pets.models import Pet, PetPhoto

admin.site.register(Pet)
admin.site.register(PetPhoto)