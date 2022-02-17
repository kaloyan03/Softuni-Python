from django.urls import path
from expenses_tracker.profiles import views


urlpatterns = [
# ⦁	http://localhost:8000/profile/ - profile page
# ⦁	http://localhost:8000/profile/edit/ - profile edit page
# ⦁	http://localhost:8000/profile/delete/ - delete profile page
    path('', views.show_profile, name='show profile'),
    path('edit/', views.edit_profile, name='edit profile'),
    path('delete/', views.delete_profile, name='delete profile'),
]