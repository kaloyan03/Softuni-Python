from django.shortcuts import render, redirect

# Create your views here.
from notes.note.forms import CreateNoteForm, EditNoteForm
from notes.note.models import Note


def create_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, id):
    note = Note.objects.get(id=id)

    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, id):
    note = Note.objects.get(id=id)

    if request.method == 'POST':
        note.delete()
        return redirect('home page')

    else:
        context = {
            'note': note,
        }

        return render(request, 'note-delete.html', context)


def show_note_details(request, id):
    note = Note.objects.get(id=id)

    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)

