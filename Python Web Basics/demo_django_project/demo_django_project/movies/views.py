from django.shortcuts import render


def list_movies(request):
    context = {
        'movies': [
            'Spider-Man',
            'Naruto',
            'Kung Fu Panda',
            'Samurai Jack',
        ]
    }

    return render(request, 'movies.html', context)
