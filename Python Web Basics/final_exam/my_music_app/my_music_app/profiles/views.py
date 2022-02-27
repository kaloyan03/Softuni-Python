from django.shortcuts import render, redirect

# Create your views here.
from my_music_app.albums.models import Album
from my_music_app.profiles.models import Profile


def get_profile():
    profiles = Profile.objects.all()

    if profiles:
        return profiles[0]


def show_profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.count()

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    albums = Album.objects.all()

    if request.method == 'POST':
        profile.delete()
        [a.delete() for a in albums]
        return redirect('home page')

    else:
        return render(request, 'profile-delete.html')
