from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from cars.models import Car
from cars.serializers import CarSerializer


class ListCreateCars(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetUpdateDeleteCar(APIView):
    def get(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response({"message": "not found"},status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)

            serializer = CarSerializer(car, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status)



        except:
            return Response({"message": "bad request"},status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        car = Car.objects.get(pk=pk)
        car.delete()
        return Response({"message": "Successfully deleted"})

