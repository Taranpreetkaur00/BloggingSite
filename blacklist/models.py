from __future__ import unicode_literals   # so that our database can adapt any language
from django.db import models
 

# Create your models here.
class Blacklist(models.Model):

    
    ip = models.CharField(max_length= 10)
    


    def __str__ (self):
        return self.ip 