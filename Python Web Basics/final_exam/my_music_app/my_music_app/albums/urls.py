from django.urls import path
from my_music_app.albums import views


urlpatterns = (
    path('add/', views.add_album, name='add album'),
    path('edit/<int:id>', views.edit_album, name='edit album'),
    path('delete/<int:id>', views.delete_album, name='delete album'),
    path('details/<int:id>', views.show_album_details, name='details album'),

)