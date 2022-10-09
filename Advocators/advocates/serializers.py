from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Advocates

def number_validator(num):
    if num < 0:
        raise ValidationError('enter valid number')

class AdvocateSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    profile_pic = serializers.ImageField()
    short_bio = serializers.CharField()
    advocate_years_exp = serializers.IntegerField(
                            validators = [number_validator]
                        )
    company = serializers.JSONField()
    links = serializers.JSONField()

    class Meta:
        model = Advocates
        fields = '__all__'
