from django.urls import path

from notes.profiles.views import show_profile, delete_profile

urlpatterns = [
    path('', show_profile, name='show profile'),
    path('delete/', delete_profile, name='delete profile'),
]