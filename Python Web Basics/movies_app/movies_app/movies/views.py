from django.shortcuts import render, redirect

from movies_app.movies.models import Movie
from movies_app.movies.movies_form import CreateMovieForm
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


def create_movie(request):
    if request.method == 'POST':
        form = CreateMovieForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image_url = form.cleaned_data['image_url']

            movie = Movie(title=title, description=description, image_url=image_url)

            movie.save()

            return redirect('list movies')
    else:
        form = CreateMovieForm()
        context = {
            'form': form
        }
        return render(request, 'create_movie_page/index.html', context)