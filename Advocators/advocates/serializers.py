import json
from django.core.exceptions import ValidationError
from rest_framework import serializers

from companies.models import Companies

from .models import Advocates

def number_validator(num):
    if num < 0:
        raise ValidationError('enter valid number')

class AdvocateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required = False)
    name = serializers.CharField()
    profile_pic = serializers.URLField()
    short_bio = serializers.CharField()
    long_bio = serializers.CharField(required = False)
    advocate_years_exp = serializers.IntegerField(validators = [number_validator])
    company = serializers.PrimaryKeyRelatedField(queryset=Companies.objects.all(), many=False , required = False)
    links = serializers.JSONField(required = False)
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        if response['company']:
            response['company'] = {
                "id" : instance.company.id,
                "name" : instance.company.name,
                "logo" : str(instance.company.logo),
                "href":"/companies/{0}".format(instance.company.id)
            }
        return response

    class Meta:
        model = Advocates
        fields = '__all__'
