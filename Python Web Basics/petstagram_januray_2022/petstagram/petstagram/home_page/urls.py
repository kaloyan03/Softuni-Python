from django.urls import path
from petstagram.home_page import views


urlpatterns = (
    path('', views.home_page, name='home page'),
)