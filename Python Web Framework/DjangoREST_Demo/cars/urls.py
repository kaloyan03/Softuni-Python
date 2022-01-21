from django.urls import path

from cars.views import ListCreateCars, GetUpdateDeleteCar

urlpatterns = (
    path('', ListCreateCars.as_view(), name='list,create cars'),
    path('<int:pk>', GetUpdateDeleteCar.as_view(), name='get,update,delete car'),
)