from django.urls import path
from todo_project.forms_page.views import show_form_data


urlpatterns = [
    path('', show_form_data, name='show form')
]