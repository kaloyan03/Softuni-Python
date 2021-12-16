from django.contrib import admin

from movies_app.movies.models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


admin.site.register(Movie, MovieAdmin)