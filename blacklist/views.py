from django.shortcuts import render , get_object_or_404,redirect  #404 for ,when we dont have database can we can handle it without showing 404
from .models import Blacklist
from blog.models import Blog
from cate.models import Cat
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User , Group ,Permission
from manager.models import Manager
import random
import string
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
# Create your views here.


def black_list(request):

    ip = Blacklist.objects.all()

    return render(request,'back/blacklist.html',{'ip':ip})

def ip_add(request):

    if request.method == 'POST':
         
        ip = request.POST.get('ip')
        
        if ip != '' :
            b= Blacklist(ip=ip)
            b.save()

    return redirect('black_list')

def ip_del(request,pk):

    b =  Blacklist.objects.filter(pk=pk)
    b.delete()

    return redirect('black_list')