from django.urls import path
from petstagram.profiles import views


urlpatterns = [
    path('', views.show_profile, name='show profile'),
]