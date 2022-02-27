from django.shortcuts import render

# Create your views here.
from my_music_app.albums.models import Album
from my_music_app.profiles.forms import CreateProfileForm
from my_music_app.profiles.views import get_profile


def home_page(request):
    profile = get_profile()
    albums = Album.objects.all()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()
            profile = get_profile()

    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'albums': albums,
    }

    if profile:
        return render(request, 'home-with-profile.html', context)
    return render(request, 'home-no-profile.html', context)