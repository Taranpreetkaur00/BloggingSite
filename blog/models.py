from __future__ import unicode_literals   # so that our database can adapt any language
from django.db import models


# Create your models here.
class Blog(models.Model):

    name = models.CharField(max_length= 200)
    short_txt = models.TextField(default='-')
    body_txt = models.TextField(default='-')
    date = models.CharField(max_length= 12)
    time = models.CharField(max_length= 12,default='00:00')
    imgname = models.TextField(default="-")
    imgurl = models.TextField(default='-')
    writer = models.CharField(max_length=50)
    category = models.CharField(max_length= 200,default='category')
    catid = models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    tag = models.TextField(default='-')
    act = models.IntegerField(default=0)
    rand = models.IntegerField(default=0)
    
    def __str__ (self):
        return self.name 