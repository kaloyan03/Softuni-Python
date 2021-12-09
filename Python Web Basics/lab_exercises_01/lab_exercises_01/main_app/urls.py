from django.urls import path
from lab_exercises_01.main_app.views import index

urlpatterns = [
    path('', index)
]
