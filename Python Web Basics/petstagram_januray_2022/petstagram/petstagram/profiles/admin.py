from django.contrib import admin

# Register your models here.
from petstagram.profiles.models import Profile

class AdminProfile(admin.ModelAdmin):
    list_display = ('id','full_name', 'gender')

admin.site.register(Profile, AdminProfile)