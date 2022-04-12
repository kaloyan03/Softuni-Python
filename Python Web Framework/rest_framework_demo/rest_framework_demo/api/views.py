from django.shortcuts import render
from rest_framework import generics as api_views
# Create your views here.
from rest_framework_demo.api.models import Animal
from rest_framework_demo.api.serializers import AnimalSerializer



class ListCreateAnimalsView(api_views.ListCreateAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()


class SingleAnimalView(api_views.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()



