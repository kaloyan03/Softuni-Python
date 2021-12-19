from django.shortcuts import render, redirect

from book_app.books.models import Book
from book_app.books.book_form import BookForm
# Create your views here.


def show_form_get(form, request, template):
    context = {
        'form': form,
    }

    return render(request, template, context)


def index(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'index.html', context)


def create_book(request):
    if request.method == 'GET':
        form = BookForm()
        return show_form_get(form, request, 'create.html')
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        return show_form_get(form, request, 'create.html')


def update_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'GET':
        form = BookForm(
            initial=book.__dict__
        )

        return show_form_get(form, request, 'update.html')
    else:
        form = BookForm(
            request.POST,
            instance=book)

        if form.is_valid():
            form.save()
            return redirect('index')

        return show_form_get(form, request, 'update.html')