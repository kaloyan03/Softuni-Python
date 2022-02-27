from django.urls import path
from my_music_app.home_page import views

urlpatterns = (
    path('', views.home_page, name='home page'),
)