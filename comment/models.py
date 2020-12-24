from __future__ import unicode_literals   # so that our database can adapt any language
from django.db import models


# Create your models here.
class Comment(models.Model):

    name = models.CharField(max_length= 50)
    email = models.CharField(max_length= 50)
    cm = models.TextField()
    blog_id = models.IntegerField()
    date = models.CharField(max_length= 12)
    time = models.CharField(max_length= 15)
    status = models.IntegerField(default=0)
    
    
    def __str__ (self):
        return self.name 