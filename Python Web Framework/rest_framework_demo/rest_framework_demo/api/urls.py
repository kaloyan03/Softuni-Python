from django.urls import path

from rest_framework_demo.api.views import ListCreateAnimalsView, SingleAnimalView

urlpatterns = [
    path('animals/', ListCreateAnimalsView.as_view(), name='animals list create'),
    path('animals/<int:pk>/', SingleAnimalView.as_view(), name='animals list create'),
]