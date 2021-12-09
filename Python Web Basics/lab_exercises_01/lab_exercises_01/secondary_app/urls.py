from django.urls import path
from lab_exercises_01.secondary_app.views import index

urlpatterns = [
    path('', index)
]
