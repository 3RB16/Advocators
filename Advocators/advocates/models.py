from importlib.metadata import requires
from django.db import models
from django.core.exceptions import ValidationError
from companies.models import Companies


# Create your models here.

def linksCallable () : 
    return {
        "youtube":"",
        "twitter":"",
        "github":"",
    }



def number_validator(num):
    if num < 0:
        raise ValidationError('enter valid number')

class Advocates(models.Model):
    name = models.CharField(max_length = 255 , null = False , blank = False)
    profile_pic = models.ImageField(null = True , unique = True)
    short_bio = models.CharField(max_length = 255 , null = True , blank = True)
    long_bio = models.TextField(blank = True , null = True)
    advocate_years_exp = models.IntegerField(null = True , validators = [number_validator])
    company = models.ForeignKey(
                    Companies, on_delete = models.SET_NULL, 
                    related_name = 'advocates' , null = True
                )
    links = models.JSONField(default = linksCallable)
    
    class Meta:
        db_table = 'advocates'

    def __str__(self):
        return self.name