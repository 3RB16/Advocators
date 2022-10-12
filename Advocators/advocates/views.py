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

class AdvocateDetail(APIView):
    pass