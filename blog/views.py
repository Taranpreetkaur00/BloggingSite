from django.shortcuts import render , get_object_or_404,redirect  #404 for ,when we dont have database can we can handle it without showing 404
from .models import Blog
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime  
from subcat.models import SubCat
from cate.models import Cat
from comment.models import Comment
from django.contrib.auth.models import User
import random
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from itertools import chain

# Create your views here.

mysearch = ""

def blog_detail(request,word):
    site= Main.objects.get(pk=1)
    blog = Blog.objects.filter(name=word)
    cat = Cat.objects.all()
    showblog = Blog.objects.filter(name=word)
    popblog = Blog.objects.all().order_by('-show')[:3]
    popblog2 = Blog.objects.all().order_by('-show')[:2]
    tagname = Blog.objects.get(name=word).tag
    tag = tagname.split(',')
    try:
        myblog = Blog.objects.get(name=word)
        myblog.show = myblog.show + 1
        myblog.save()
    except:
        print("Can't add show")

    code = Blog.objects.get(name=word).pk
    comment = Comment.objects.filter(blog_id=code , status=1).order_by('-pk')[:5]
    cmcount = len(comment)

    link = "/urls/" + str(Blog.objects.get(name=word).rand)

    return render(request,'front/blog_detail.html',{'blog':blog ,'comment':comment,'site':site,'cat':cat,'popblog':popblog,'showblog':showblog,'popblog2':popblog2,'tag':tag ,'cmcount':cmcount,'code':code,'link':link,'tagname':tagname})

def blog_detail_short(request,pk):

    site= Main.objects.get(pk=1)

    blog = Blog.objects.all().order_by('-pk')
    showblog = Blog.objects.filter(rand=pk)
    cat = Cat.objects.all()
    popblog = Blog.objects.all().order_by('-show')[:3]
    popblog2 = Blog.objects.all().order_by('-show')[:2]
    tagname = Blog.objects.get(rand=pk).tag
    tag = tagname.split(',')
    try:
        myblog = Blog.objects.get(rand=pk)
        myblog.show = myblog.show + 1
        myblog.save()
    except:
        print("Can't add show")

    link = "/urls/" + str(Blog.objects.get(name=word).rand)

    return render(request,'front/blog_detail.html',{'blog':blog ,'site':site,'cat':cat,'showblog':showblog,'popblog':popblog,'popblog2':popblog2,'tag':tag ,'link':link})


def blog_list(request):

    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1
    
    if perm == 0:
        blog = Blog.objects.filter(writer=request.user)

    elif perm == 1:
        blogs = Blog.objects.all()        
        paginator = Paginator(blogs,2)
        page = request.GET.get('page')

        try:
            blog = paginator.page(page)

        except EmptyPage :
            blog = paginator.page(paginator.num_page)
        
        except PageNotAnInteger:
            blog = paginator.page(1)
        

    return render(request,'back/blog_list.html',{'blog':blog})

def blog_add (request):
    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end
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
   
    date = str(year) + str(month) + str(day) 
    randint = str(random.randint(1000,9999))
    rand = date + randint
    rand = int(rand)

    while len(Blog.objects.filter(rand=rand)) != 0:
        randint = str(random.randint(1000,9999))
        rand = date + randint
        rand = int(rand)


    cat = SubCat.objects.all()

    if request.method =='POST':
        blogtitle = request.POST.get('blogtitle')
        blogcat = request.POST.get('blogcat')
        blogtxtshort = request.POST.get('blogtxtshort')
        blogtxt = request.POST.get('blogtxt')
        blogid = request.POST.get('blogcat')
        tag = request.POST.get('tag')
        
        if blogtitle == "" or blogtxtshort == "" or blogtxt == "" or blogcat == "":
            error = "All Fields Required"
            return render(request,'back/error.html',{'error':error})

        try:    
            myfile = request.FILES['myfile'] # taking file
            fs = FileSystemStorage()   #making object
            filename = fs.save(myfile.name,myfile)
            url = fs.url(filename)   #creating path for file

            if str(myfile.content_type).startswith('image'):    # checking if file that has been uploaded is img or not

                if myfile.size < 5000000:
                    blogname =SubCat.objects.get(pk=blogid).name
                    ocatid = SubCat.objects.get(pk=blogid).catid
                    b = Blog(name=blogtitle,tag=tag,short_txt=blogtxtshort,time = time,body_txt=blogtxt,date=today,imgname=filename ,imgurl=url,writer=request.user,category=blogname,catid=blogid,show=0 ,rand=rand,ocatid=ocatid)
                    b.save()
                    
                    count = len(Blog.objects.filter(ocatid=ocatid))
                    b = Cat.objects.get(pk=ocatid)
                    b.count = count
                    b.save()
                    return redirect('blog_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "Your File is Bigger than 5MB!!"
                    return render(request,'back/error.html',{'error':error})    

            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File should be an Image!!"
                return render(request,'back/error.html',{'error':error})

        except:
            error = "Please Choose an Image!!"
            return render(request,'back/error.html',{'error':error})
    return render (request,'back/blog_add.html',{'cat':cat})



def blog_edit(request,pk):
    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end

    if len(Blog.objects.filter(pk=pk))==0:
        error = "Blog Not Found !!"
        return render(request,'back/error.html',{'error':error})

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1
    
    if perm == 0:
        a = Blog.objects.get(pk=pk).writer
        if str(a) != str(request.user) :
            error = "Access Denied"
            return render(request, 'back/error.html',{'error':error})

    blog = Blog.objects.get(pk=pk)
    cat = SubCat.objects.all()
    if request.method =='POST':
        blogtitle = request.POST.get('blogtitle')
        blogcat = request.POST.get('blogcat')
        blogtxtshort = request.POST.get('blogtxtshort')
        blogtxt = request.POST.get('blogtxt')
        blogid = request.POST.get('blogcat')
        tag = request.POST.get('tag')
        
        if blogtitle == "" or blogtxtshort == "" or blogtxt == "" or blogcat == "":
            error = "All Fields Required"
            return render(request,'back/error.html',{'error':error})

        try:    
            myfile = request.FILES['myfile'] # taking file
            fs = FileSystemStorage()   #making object
            filename = fs.save(myfile.name,myfile)
            url = fs.url(filename)   #creating path for file

            if str(myfile.content_type).startswith('image'):    # checking if file that has been uploaded is img or not

                if myfile.size < 5000000:
                    blogname =SubCat.objects.get(pk=blogid).name
                    
                    fss = FileSystemStorage()
                    fss.delete(b.imgname)

                    b = Blog.objects.get(pk=pk)
                    b.name = blogtitle
                    b.short_txt = blogtxtshort
                    b.body_txt = blogtxt
                    b.category = blogname
                    b. imgname = filename
                    b.imgurl = url
                    b.tag = tag
                    b.catid = blogid

                    b.save()
                    return redirect('blog_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "Your File is Bigger than 5MB!!"
                    return render(request,'back/error.html',{'error':error})    

            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File should be an Image!!"
                return render(request,'back/error.html',{'error':error})

        except:
            blogname =SubCat.objects.get(pk=blogid).name

            b = Blog.objects.get(pk=pk)

            b.name = blogtitle
            b.short_txt = blogtxtshort
            b.body_txt = blogtxt
            b.category = blogname
            b.catid = blogid
            b.tag = tag
            b.act = 0
            b.save()
            return redirect('blog_list')
    return render (request,'back/blog_edit.html',{'cat':cat,'blog':blog,'pk':pk})

def blog_delete(request,pk):
    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1
    
    if perm == 0:
        a = Blog.objects.get(pk=pk).writer
        if str(a) != str(request.user) :
            error = "Access Denied"
            return render(request, 'back/error.html',{'error':error})

    try:
        b = Blog.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(b.imgname)

        ocatid = Blog.objects.get(pk=pk).ocatid

        b.delete()

        count = len(Blog.objects.filter(ocatid=ocatid))
        m = Cat.objects.get(pk=ocatid)
        m.count = count
        m.save()
    except:
        error = "Something Wrong!!"
        return render(request,'back/error.html',{'error':error})

    return redirect('blog_list')
   

def blog_publish(request,pk):
    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end
    
    blog = Blog.objects.get(pk=pk)
    blog.act=1
    blog.save()

    return redirect('blog_list')

def blog_all_show(request,word):

    catid = Cat.objects.get(name=word).pk
    allblog = Blog.objects.filter(ocatid=catid)

    site= Main.objects.get(pk=1)
    blog = Blog.objects.filter(act=1).order_by('-pk')
    blog2 = Blog.objects.filter(act=1).order_by('-pk')[:3]
    cat = Cat.objects.all()
    lastblog = Blog.objects.filter(act=1).order_by('-pk')[:2]
    popblog = Blog.objects.filter(act=1).order_by('-show')[:3]
    
    return render(request,'front/all_blog.html',{'site':site,'blog':blog,'cat':cat,'lastblog':lastblog, 'popblog':popblog, 'blog2':blog2,'allblog':allblog})

def all_blog(request):

    allblog = Blog.objects.all()

    site= Main.objects.get(pk=1)
    blog = Blog.objects.filter(act=1).order_by('-pk')
    blog2 = Blog.objects.filter(act=1).order_by('-pk')[:3]
    cat = Cat.objects.all()
    lastblog = Blog.objects.filter(act=1).order_by('-pk')[:2]
    popblog = Blog.objects.filter(act=1).order_by('-show')[:3]
    
    return render(request,'front/all_blog2.html',{'site':site,'blog':blog,'cat':cat,'lastblog':lastblog, 'popblog':popblog, 'blog2':blog2,'allblog':allblog})

def all_blog_search(request):

    if request.method == 'POST':
        text = request.POST.get('text')
        catid = request.POST.get('cat')
        mysearch = text

        if catid == '0':
            a = Blog.objects.filter(name__contains=text)
            b = Blog.objects.filter(short_txt__contains=text)
            c = Blog.objects.filter(body_txt__contains=text)
        else:
            a = Blog.objects.filter(name__contains=text,ocatid=catid)
            b = Blog.objects.filter(short_txt__contains=text,ocatid=catid)
            c = Blog.objects.filter(body_txt__contains=text,ocatid=catid)

        allblogs = list(chain(a,b,c))
        allblogs = list(dict.fromkeys(allblogs))
    
    else :
        if catid == '0':
            a = Blog.objects.filter(name__contains=mysearch)
            b = Blog.objects.filter(short_txt__contains=mysearch)
            c = Blog.objects.filter(body_txt__contains=mysearch)
        else:
            a = Blog.objects.filter(name__contains=mysearch,ocatid=catid)
            b = Blog.objects.filter(short_txt__contains=mysearch,ocatid=catid)
            c = Blog.objects.filter(body_txt__contains=mysearch,ocatid=catid)

        allblogs = list(chain(a,b,c))
        allblogs = list(dict.fromkeys(allblogs))

    site= Main.objects.get(pk=1)
    blog = Blog.objects.filter(act=1).order_by('-pk')
    blog2 = Blog.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    lastblog = Blog.objects.filter(act=1).order_by('-pk')[:2]
    popblog = Blog.objects.filter(act=1).order_by('-show')[:3]

    
    paginator = Paginator(allblogs,12)
    page = request.GET.get('page')

    try:
        allblog = paginator.page(page)

    except EmptyPage :
        allblog = paginator.page(paginator.num_page)
        
    except PageNotAnInteger:
        allblog = paginator.page(1)
    
    return render(request,'front/all_blog2.html',{'site':site,'blog':blog,'cat':cat,'lastblog':lastblog, 'popblog':popblog, 'blog2':blog2,'allblog':allblog})

  