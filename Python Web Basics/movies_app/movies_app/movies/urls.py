from django.urls import path

from movies_app.movies.views import show_movies, load_home_page, movie_details

urlpatterns = [
    path('', load_home_page, name='home page'),
    path('movies/', show_movies, name='list movies'),
    path('movie/<int:pk>', movie_details, name='movie details'),
]