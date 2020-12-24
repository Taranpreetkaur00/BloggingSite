from django.shortcuts import render , get_object_or_404,redirect  #404 for ,when we dont have database can we can handle it without showing 404
from .models import ContactForm
from blog.models import Blog
from cate.models import Cat
from subcat.models import SubCat
import datetime  
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage



def contact_add (request):

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day= now.day
    if len(str(day)) == 1:
        day = "0" +str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)
    
    today = str(year) + "/" + str(month) + "/" + str(day) 
    time = str(now.hour) + ':' + str(now.minute)

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        txt = request.POST.get('msg')

        if name == '' or email == '' or subject == '' or txt == '':
            message = 'All Fields are Required'
            return render(request,'front/msgbox.html',{'message':message})   

        b = ContactForm(name=name,email=email,subject=subject,txt=txt,date=today,time=time)
        b.save()
        message = 'Your Message has been Received'
        return render(request,'front/msgbox.html',{'message':message}) 

    return render(request,'front/msgbox.html')

def contact_show (request):

    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end 

    msg = ContactForm.objects.all()


    return render(request,'back/contact_form.html',{'msg':msg})

def contact_del(request,pk):

    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end 

    b = ContactForm.objects.filter(pk=pk)
    b.delete()

    return redirect ('contact_show')

