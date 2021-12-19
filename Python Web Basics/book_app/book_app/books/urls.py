from django.urls import path, include
from book_app.books.views import index, create_book, update_book

urlpatterns = [
    path('', index, name='index'),
    path('create-book/', create_book, name='create book'),
    path('update-book/<int:pk>', update_book, name='update book'),
]