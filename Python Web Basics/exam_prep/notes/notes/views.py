from django.shortcuts import render

from notes.note.models import Note
from notes.profiles.forms import CreateProfileForm
from notes.profiles.views import get_profile


def create_profile(form):
    if form.is_valid():
        form.save()


def home_page(request):
    profile = get_profile()
    notes = Note.objects.all()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        create_profile(form)
        return render(request, 'home-with-profile.html')

    else:
        form = CreateProfileForm()

        context = {
            'form': form,
            'notes': notes,
        }

        if profile:
            return render(request, 'home-with-profile.html', context)
        return render(request, 'home-no-profile.html', context)