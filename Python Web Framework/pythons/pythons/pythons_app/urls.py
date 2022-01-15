from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('create/', views.CreatePython.as_view(), name="create")
]
