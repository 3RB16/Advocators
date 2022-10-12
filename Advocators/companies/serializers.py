from rest_framework import serializers
from .models import Companies
from advocates.serializers import AdvocateSerializer

class CompanySerializer(serializers.ModelSerializer):
    advocates = AdvocateSerializer(many=True, read_only=True)

    class Meta:
        model = Companies
        fields = ['id', 'name', 'logo' , 'summary' , 'advocates']