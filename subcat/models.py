from __future__ import unicode_literals   # so that our database can adapt any language
from django.db import models
 

# Create your models here.
class SubCat(models.Model):

    name = models.CharField(max_length= 200)
    catname = models.CharField(max_length= 200)
    catid = models.CharField(max_length= 200)
    

    def __str__ (self):
        return self.name 