from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from companies.models import Companies
from .models import *
from .serializers import *
import json
# Create your views here.


class AdvocateList(APIView):
    def get(self , request):
        serializer = AdvocateSerializer(Advocates.objects.all() , many = True)
        return Response(serializer.data , status = status.HTTP_200_OK) 
    
    def post(self , request):
        serializer = AdvocateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self , data):
        Advocates.objects.all().delete()
        return Response(data = {'message' : 'deleted'} , status = status.HTTP_200_OK)

class AdvocateDetail(APIView):
    def get(self , request , pk):
        try:
            serializer = AdvocateSerializer(Advocates.objects.get(id = pk))
        except Advocates.DoesNotExist:
            return Response(data = {'message' : 'advocate not found'} , status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data , status=status.HTTP_302_FOUND)

    def delete(self , request , pk):
        try:
            Advocates.objects.get(id = pk).delete()
        except Advocates.DoesNotExist:
            return Response(data = {'message' : 'advocate not found'} , status=status.HTTP_404_NOT_FOUND)
        return Response(data = {'message' : 'deleted'} , status = status.HTTP_200_OK)
    
    def put(self , request , pk):
        try:
            serializer = AdvocateSerializer(data = request.data,instance = Advocates.objects.get(id = pk))    
            if serializer.is_valid():
                serializer.save()
                return Response(data = {'message' : 'advocate updated'} , status=status.HTTP_200_OK)
        except Advocates.DoesNotExist:
            return Response(data = {'message' : 'advocate not found'} , status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)