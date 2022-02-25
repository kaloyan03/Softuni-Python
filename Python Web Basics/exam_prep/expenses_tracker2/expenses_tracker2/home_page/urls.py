from django.urls import path
from expenses_tracker2.home_page import views

urlpatterns = (
    path('', views.index, name='index'),
)