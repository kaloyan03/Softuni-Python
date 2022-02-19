from django.urls import path
from expenses_tracker.expenses import views

urlpatterns = [
    path('create/', views.create_expense, name='create expense'),
    path('edit/<int:id>', views.edit_expense, name='edit expense'),
    path('delete/<int:id>', views.delete_expense, name='delete expense'),
]