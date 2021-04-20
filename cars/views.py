from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Car
from .serializer import CarSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def car_get(request):
  
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializers(cars, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
        serializer = CarSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@api_view(['POST'])
def car_post(request):
    if request.method == 'POST':
        
        serializer = CarSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@api_view(['GET'])
def car_get_car(request, id):
  
    if request.method == 'GET':
        car = Car.objects.get(id = id)
        serializer = CarSerializers(car)
        return Response(serializer.data)