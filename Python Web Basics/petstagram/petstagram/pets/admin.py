from django.contrib import admin
from petstagram.pets.models import Pet


# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', 'age']



admin.site.register(Pet, PetAdmin)