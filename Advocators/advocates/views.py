from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

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
    
    def delete(self , request):
        try:
            Advocates.objects.all().delete()
        except  Advocates.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        return Response(status = status.HTTP_202_ACCEPTED)

class AdvocateDetail(APIView):
    def get(self , request , pk):
        try:
            serializer = AdvocateSerializer(Advocates.objects.get(pk = pk))
        except Advocates.DoesNotExist:
            return Response(data = {"message" : "Advocate Not Found"} , status = status.HTTP_404_NOT_FOUND)
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    def put(self , request , pk):
        serializer = AdvocateSerializer(
                        data = request.data, 
                        instance=Advocates.objects.get(id = pk)
                    )
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk):
        try:
            Advocates.objects.get(id = pk).delete()
        except Advocates.DoesNotExist:
            return  Response(status = status.HTTP_404_NOT_FOUND)
        return Response(status = status.HTTP_200_OK)
