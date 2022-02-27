from django.shortcuts import render

# Create your views here.
from my_music_app.profiles.models import Profile


def get_profile():
    profiles = Profile.objects.all()

    if profiles:
        return profiles[0]


def show_profile_details(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    pass
