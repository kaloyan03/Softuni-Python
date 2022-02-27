from django.shortcuts import render, redirect

# Create your views here.
from my_music_app.albums.forms import AddAlbumForm, EditAlbumForm, DeleteAlbumForm
from my_music_app.albums.models import Album


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
    album = Album.objects.get(id=id)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'edit-album.html', context)




def show_album_details(request, id):
    album = Album.objects.get(id=id)

    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


def delete_album(request, id):
    album = Album.objects.get(id=id)

    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        form.save()
        return redirect('home page')

    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'delete-album.html', context)