from django.shortcuts import render , get_object_or_404,redirect  #404 for ,when we dont have database can we can handle it without showing 404
from .models import Newsletter
from blog.models import Blog
from cate.models import Cat
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,Group,Permission
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail

# Create your views here.

def news_letter(request):

    if request.method == 'POST':
        txt = request.POST.get('txt')

        b = Newsletter(txt=txt)
        b.save()

    return redirect('home')

def news_emails(request):

    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end 

    emails = Newsletter.objects.all()


    return render (request,'back/emails.html',{'emails':emails})

def news_txt_del(request,pk):

    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end 

    b = Newsletter.objects.get(pk=pk)
    b.delete()


    return redirect ('news_emails')

def send_email(request):

    if request.method == 'POST':

        txt = request.POST.get('txt')

        a = []
        for i in Newsletter.objects.all():
            a.append(Newsletter.objects.get(pk=i.pk).txt)
        print(a)

        send_mail(
            'testing mails ',
            txt,
            'tkaur447@gmail.com',
            [a],
            fail_silently = False,
        )

    return redirect('news_emails')

def check_mychecklist(request):

    if request.method == "POST":

        '''for i in Newsletter.objects.all():
            x = request.POST.get(str(i.pk))
            print(x)
            if x == 'on' :
                b = Newsletter.objects.get(pk=i.pk)
                b.delete()'''
        
        check = request.POST.getlist('checks[]')
        print(check)
        for i in check:
            b = Newsletter.objects.get(pk=i).txt
            b.delete()
   
    
    return redirect('news_emails')