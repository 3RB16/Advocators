from email.policy import default
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
import json

class Companies(models.Model):
    name = models.CharField(max_length = 255)
    logo = models.ImageField()
    summary = models.TextField(blank = True) 
    
    class Meta:
        db_table = 'companies'
    
    def __str__(self):
        return self.name