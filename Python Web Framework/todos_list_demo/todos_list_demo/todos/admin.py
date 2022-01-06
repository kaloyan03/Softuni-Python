from django.contrib import admin

# Register your models here.
from todos_list_demo.todos.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_completed']


admin.site.register(Todo, TodoAdmin)