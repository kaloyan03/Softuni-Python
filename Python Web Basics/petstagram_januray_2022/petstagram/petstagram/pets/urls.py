from django.urls import path
from petstagram.pets import views


urlpatterns = (
    path('dashboard/', views.pets_dashboard, name='pet dashboard'),
)