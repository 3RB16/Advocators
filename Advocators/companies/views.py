from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.


class CompanyList(APIView):
    def get(self , request):
        serializer = CompanySerializer(Companies.objects.all() , many = True)
        return Response(serializer.data , status = status.HTTP_200_OK) 
    
    def post(self , request):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self , data):
        Companies.objects.all().delete()
        return Response(data = {'message' : 'deleted'} , status = status.HTTP_200_OK)

class CompanyDetail(APIView):
    def get(self , request , pk):
        try:
            serializer = CompanySerializer(Companies.objects.get(id = pk))
        except Companies.DoesNotExist:
            return Response(data = {'message' : 'Company not found'} , status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data , status=status.HTTP_302_FOUND)

    def delete(self , request , pk):
        try:
            Companies.objects.get(id = pk).delete()
        except Companies.DoesNotExist:
            return Response(data = {'message' : 'Company not found'} , status=status.HTTP_404_NOT_FOUND)
        return Response(data = {'message' : 'deleted'} , status = status.HTTP_200_OK)
    
    def put(self , request , pk):
        try:
            serializer = CompanySerializer(data = request.data,instance = Companies.objects.get(id = pk))    
            if serializer.is_valid():
                serializer.save()
                return Response(data = {'message' : 'Company updated'} , status=status.HTTP_200_OK)
        except Companies.DoesNotExist:
            return Response(data = {'message' : 'Company not found'} , status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
