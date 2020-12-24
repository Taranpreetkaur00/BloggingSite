from __future__ import unicode_literals   # so that our database can adapt any language
from django.db import models
 

# Create your models here.
class Newsletter(models.Model):

    
    txt = models.CharField(max_length= 100)
    

    def __str__ (self):
        return self.txt