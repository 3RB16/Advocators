from email.policy import default
from wsgiref.validate import validator
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def links_content () : 
    return {
        "youtube":"",
        "twitter":"",
        "github":"",
    }
def company_content():
    return {
        "id": None,
        "name":"",
        "logo":"",
        "href":"",
    }

def number_validator(num):
    if num < 0:
        raise ValidationError('enter valid number')


class Advocates(models.Model):
    name = models.CharField(max_length = 255)
    profile_pic = models.ImageField(unique = True)
    short_bio = models.CharField(max_length = 255 , null = True)
    long_bio = models.TextField(blank = True , null = True)
    advocate_years_exp = models.IntegerField(null = True , validators = [number_validator])
    company = models.JSONField(default = company_content)
    links = models.JSONField(default = links_content)
    
    class Meta:
        db_table = 'advocates'

    def __str__(self):
        return self.name