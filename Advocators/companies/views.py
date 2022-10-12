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


class CompanyDetail(APIView):
    pass 
