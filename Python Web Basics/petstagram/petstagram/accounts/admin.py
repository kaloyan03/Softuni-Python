from django.contrib import admin

# Register your models here.
from petstagram.accounts.models import UserProfile

admin.site.register(UserProfile)