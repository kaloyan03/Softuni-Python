from django.contrib import admin

# Register your models here.
from todos.todo.models import Todo

admin.site.register(Todo)