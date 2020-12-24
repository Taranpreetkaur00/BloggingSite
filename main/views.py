from django.shortcuts import render , get_object_or_404,redirect  #404 for ,when we dont have database can we can handle it without showing 404
from .models import Main
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
from django.core.mail import send_mail
from contactform.models import ContactForm
from zeep import Client 
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup 
import urllib.request as urllib2 
from rest_framework import viewsets
from .serializer import BlogSerializer
from django.http import JsonResponse
from newsletter.models import Newsletter

# Create your views here.

@csrf_exempt
def home(request):
    site= Main.objects.get(pk=1)
    blog = Blog.objects.filter(act=1).order_by('-pk')
    blog2 = Blog.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    lastblog = Blog.objects.filter(act=1).order_by('-pk')[:2]
    popblog = Blog.objects.filter(act=1).order_by('-show')[:3]

    #soup
    '''client = Client('xxxxxxxx.wsdl')
    result = client.service.funcname(1,2,3)
    print(result)'''
    #curl
    '''url = 'xxxxxxxxxxxxxxx'
    payload = {'a':b,'c':d}
    result = requests.post(url,params=payload)
    print(result.url)
    print(result)'''
    #json
    '''url= 'xxxxxxxxxxxxxx'
    data = {'a':"b",'c':"d"}
    headers = {'Content-Type' :'application/json','API_KEY':'xxxxxxxxxxxxxx'}
    result = requests.post(url,data=json.dumps(data),headers=headers)
    print(result)'''

    #BSP4
   # my_html = 
    """
    <html>
    <head>
    <title> This is a Test </title>
    </head>
    </html>
    """
    #soup = BeautifulSoup(my_html,'html.parser')
    #print(soup.title.string)
    #print(soup.title.parent.name)
    #print(soup.p['class'])
    #print(soup.a) ; print(soup.find_all('a'))
    #print(soup.find(id="link1"))

    #url = "https://www.w3school.com/"
    #result = requests.post(url)
    #print(result.content)
    
    '''url = "https://www.w3schools.com/"
    opener = urllib2.build_opener()
    content = opener.open(url).read()
    soup = BeautifulSoup(content)
    print(soup.title.string)'''

    #for collecting json text 
    #url = "http://127.0.0.1:8000/show/data/"
    #opener = urllib2.build_opener()
    #content = opener.open(url).read()    
    #print(content)

    request.session['test' ] = 'hello'
    print(request.session['test'])
    

    return render(request,'front/home.html',{'site':site,'blog':blog,'cat':cat,'lastblog':lastblog, 'popblog':popblog, 'blog2':blog2})

def about(request):
    site= Main.objects.get(pk=1)
    cat = Cat.objects.all()
    popblog = Blog.objects.all().order_by('-show')[:3]
    mostblog = Blog.objects.all().order_by('-show')[:4]
    return render(request,'front/about.html',{'site':site,'popblog':popblog,'cat':cat,'mostblog':mostblog})



def panel(request):

    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end    

    perm = 0
    perms = Permission.objects.filter(user=request.user)
    for i in perms :
        if i.codename == 'master_user' : perm = 1

    return render(request,'back/home.html',{})

def my_login (request):

    if request.method == 'POST':
        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')

        if utxt != "" and ptxt != "":
            user = authenticate(username=utxt,password=ptxt)

            if user != None :
                login(request, user)
                return redirect('panel')

    return render( request, 'front/login.html')

def my_logout (request):

    logout(request)

    return redirect('my_login')

def site_setting(request):

    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end 

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1
    
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html',{'error':error})

    if request.method == "POST":

        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb   = request.POST.get('fb')
        tw   = request.POST.get('tw')
        lkdn = request.POST.get('lkdn')
        link = request.POST.get('link')
        txt  = request.POST.get('txt')

        seo_txt  = request.POST.get('seotxt')
        seo_keywords = request.POST.get('seokeyword')

        if fb ==  '' : fb = '#'
        if tw == ''  : tw = '#'
        if lkdn == '' : lkdn = '#'
        if link == '' : link = '#'

        if name == "" or tell == "" or txt == "":
            error = "All Fields are Required!"
            return render(request, 'back/error.html',{'error':error})

        try:    
            myfile = request.FILES['myfile'] # taking file
            fs = FileSystemStorage()   #making object
            filename = fs.save(myfile.name,myfile)
            url = fs.url(filename)   #creating path for file

            b = Main.objects.get(pk=1)
            b.name = name
            b.tell = tell
            b.fb = fb
            b.tw = tw
            b.lkdn = lkdn
            b.link = link
            b.about = txt
            b.seo_txt = seo_txt
            b.seo_keywords = seo_keywords
            b.imgurl = url
            b.imgname = filename
            b.save()

        except :
            b = Main.objects.get(pk=1)
            b.name = name
            b.tell = tell
            b.fb = fb
            b.tw = tw
            b.lkdn = lkdn
            b.link = link
            b.about = txt
            
            b.seo_txt = seo_txt
            b.seo_keywords = seo_keywords

            b.save()

    site = Main.objects.get(pk=1)    

    return render(request,'back/setting.html',{'site':site})

def about_setting(request):


    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end 

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1
    
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html',{'error':error})

    if request.method == "POST":

        txt = request.POST.get('txt')
    
        if txt == "":
            error = "All Fields are Required!"
            return render(request, 'back/error.html',{'error':error})

        b = Main.objects.get(pk=1)
        b.abouttxt = txt 
        b.save()
    about = Main.objects.get(pk=1).abouttxt

    return render(request,'back/about_setting.html',{'about':about})

def contact_us (request):

    site= Main.objects.get(pk=1)
    cat = Cat.objects.all()
    popblog = Blog.objects.all().order_by('-show')[:3]

    return render(request,'front/Contact_us.html',{'site':site,'cat':cat,'popblog':popblog})

def change_pass (request):

    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end 

    if request.method == 'POST':

        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')

        if oldpass == '' or newpass == '':
            error = "All Fields are Required!"
            return render(request, 'back/error.html',{'error':error})
        
        user = authenticate(username=request.user,password=oldpass)

        if user != None :
    
            if len(newpass) < 8:
                error = "Your  Password must contain at least 8 character !!"
                return render(request, 'back/error.html',{'error':error})

            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            for i in newpass:
                
                if i >'0' and i <'9':
                    count1 = 1
                if i >'A' and i < 'Z':
                    count2 = 1
                if i >'a' and i <'z':
                    count3 = 1
                if i > '!' and i <'(':
                    count4 = 1

            if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1:

                user = User.objects.get(username= request.user)
                user.set_password(newpass)
                user.save()
                return redirect('my_logout')

        else :
    
            error = "Your Old Password Is Not Correct !!"
            return render(request, 'back/error.html',{'error':error})              

    return render(request,'back/changepass.html')

def my_registration(request):

    if request.method == 'POST' :

        uname = request.POST.get('uname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2 :

            message = "Your Password Didn't Match!!"
            return render(request,'front/msgbox.html',{'message':message})

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for i in password1:
                
            if i>'0' and i<'9':
                count1 = 1
            if i>'A' and i<'Z':
                count2 = 1
            if i>'a' and i<'z':
                count3 = 1
            if i>'!' and i<'(':
                count4 = 1

            
        if count1 == 0 or count2 == 0 or count3 == 0 or count4 == 0:
            message = "Your Password is not Strong!!"
            return render(request,'front/msgbox.html',{'message':message})
        
        if len(password1) < 8 :
            message = "Your  Password must contain at least 8 character !!"
            return render(request, 'front/msgbox.html',{'message':message})

        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0:
            
            ip, is_routable = get_client_ip(request)
    
            if ip is None:
                ip = '0.0.0.0'

            try:
                response = DbIpCity.get(ip,api_key='free')
                country = response.country + " | " + response.city

            except:
                country = "Unknown"
            
            user = User.objects.create_user(username=uname,email=email,password=password1)
            b = Manager(name=name,utxt=uname,email=email,ip=ip,country=country)
            b.save()
        
        return redirect('my_login')

    return render (request,'front/registration.html')

def answer_cm(request,pk):

    if request.method =='POST':
        txt = request.POST.get('txt')

        if txt == '':
            error = "Type Your Answer.."
            return render(request, 'back/error.html',{'error':error})
        
        to_email = ContactForm.objects.get(pk=pk).email
        
        send_mail(
            'testing mails ',
            txt,
            'tkaur447@gmail.com',
            [to_email],
            fail_silently = False,
        )

    return render(request,'back/answer_cm.html',{'pk':pk})

# connecting to serializer
class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 

def show_data(request):

    count = Newsletter.objects.all().count()

    data = {'count':count}

    return JsonResponse(data)