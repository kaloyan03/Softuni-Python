from django.urls import path

from rest_framework_demo.web.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]