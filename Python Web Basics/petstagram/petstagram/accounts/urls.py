from django.urls import path
from petstagram.accounts import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign up'),
    path('sign_in/', views.sign_in, name='sign in'),
    path('sign_out/', views.sign_out, name='sign out'),
    path('profile/<int:pk>', views.profile, name='profile'),
]