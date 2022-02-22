from django.urls import path
from petstagram.pets import views


urlpatterns = (
    path('dashboard/', views.pets_dashboard, name='pet dashboard'),
    path('photo/<int:id>', views.pets_photo_page, name='pet photo details')
)