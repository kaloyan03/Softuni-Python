from django.contrib import admin
from todo_project.todo_app import models
# Register your models here.
admin.site.register(models.Todo)
admin.site.register(models.Person)