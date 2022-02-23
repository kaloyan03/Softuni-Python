from django.shortcuts import render, redirect

# Create your views here.
from notes.note.models import Note
from notes.profiles.forms import CreateProfileForm
from notes.profiles.models import Profile


def get_profile():
    profiles = Profile.objects.all()

    if profiles:
        return profiles[0]
    return None


def show_profile(request):
    profile = get_profile()
    notes = Note.objects.all()

    notes_count = len(notes)

    context = {
        'notes_count': notes_count,
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()

    profile.delete()
    [note.delete() for note in notes]
    return redirect('home page')