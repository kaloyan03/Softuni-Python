from django.contrib import admin
from django.urls import path
from demo_django_project.movies.views import list_movies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', list_movies),
]
