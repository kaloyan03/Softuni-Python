from django.shortcuts import render

# Create your views here.
from petstagram.profiles.models import Profile


def get_profile():
    profile = Profile.objects.all()

    if profile:
        return profile
    return None