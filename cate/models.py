from __future__ import unicode_literals   # so that our database can adapt any language
from django.db import models
 

# Create your models here.
class Cat(models.Model):

    name = models.CharField(max_length= 200)
    count = models.IntegerField(default=0)

    def __str__ (self):
        return self.name 