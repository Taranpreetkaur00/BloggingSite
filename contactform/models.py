from __future__ import unicode_literals   # so that our database can adapt any language
from django.db import models
 

# Create your models here.
class ContactForm(models.Model):

    name = models.CharField(max_length= 50)
    email = models.CharField(max_length= 50)
    subject = models.CharField(max_length= 50)
    txt = models.TextField(max_length= 500)
    date = models.CharField(max_length= 50,default='')
    time = models.CharField(max_length= 50,default='')
    
    def __str__ (self):
        return self.name 