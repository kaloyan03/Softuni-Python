from django.contrib import admin

from book_app.books.models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'pages', 'description', 'author']


admin.site.register(Book, BookAdmin)
