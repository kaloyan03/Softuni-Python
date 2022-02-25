from django.urls import path

from expenses_tracker2.profiles import views

urlpatterns = (
    path('', views.show_profile, name='show profile'),
    path('edit/', views.edit_profile, name='edit profile'),
    path('delete/', views.delete_profile, name='delete profile'),
)