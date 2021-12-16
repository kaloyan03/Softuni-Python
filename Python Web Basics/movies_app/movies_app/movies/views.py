from django.shortcuts import render

from movies_app.movies.models import Movie
# Create your views here.


def load_home_page(request):
    return render(request, 'home_page/index.html')


def show_movies(request):
    movies = Movie.objects.all()

    context = {
        "movies": movies,
    }

    return render(request, 'movies_page/index.html', context)


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)

    context = {
        "movie": movie,
    }

    return render(request, 'movie_details/index.html', context)