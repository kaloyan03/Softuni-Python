from django.shortcuts import render, redirect

# Create your views here.
from my_music_app.albums.forms import AddAlbumForm


def add_album(request):
    if request.method == 'POST':
        form = AddAlbumForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = AddAlbumForm()
    context = {
        'form': form,
    }

    return render(request, 'add-album.html', context)

def edit_album(request, id):
    pass


def show_album_details(request, id):
    pass


def delete_album(request, id):
    pass