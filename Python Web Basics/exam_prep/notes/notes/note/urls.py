from django.urls import path
from notes.note import views

urlpatterns = [
    path('add/', views.create_note, name='create note'),
    path('edit/<int:id>', views.edit_note, name='edit note'),
    path('delete/<int:id>', views.delete_note, name='delete note'),
    path('details/<int:id>', views.show_note_details, name='details note'),
]