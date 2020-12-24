from __future__ import unicode_literals   # so that our database can adapt any language
from django.db import models
 

# Create your models here.
class Main(models.Model):

    name = models.CharField(max_length= 30)
    about = models.TextField()
    abouttxt = models.TextField(default='')
    fb = models.CharField(max_length= 30,default='FaceBook')
    lkdn = models.CharField(max_length= 30,default='LinkdIn')
    tw = models.CharField(max_length= 30,default='Twitter')
    tell = models.CharField(max_length= 30,default='contact number')
    add = models.CharField(max_length= 500,default='Address here')
    eml = models.CharField(max_length= 100,default='Your Email here')
    link =models.CharField(max_length= 30,default='any link here')

    seo_txt =models.CharField(max_length= 200,default='-')
    seo_keywords =models.TextField(default='-')

    set_name = models.CharField(max_length= 30,default='setting')
    imgurl = models.TextField(default=" ")
    imgname = models.TextField(default=" ")
    def __str__ (self):
        return self.set_name + " | " +  str(self.pk)