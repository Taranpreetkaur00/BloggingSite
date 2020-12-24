from django.shortcuts import render , get_object_or_404,redirect  #404 for ,when we dont have database can we can handle it without showing 404
from .models import Cat
import csv
from django.http import HttpResponse

def cat_list(request):
    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end
    cat = Cat.objects.all()
    return render(request,'back/cat_list.html',{'cat':cat})

def cat_add(request):
    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end
    if request.method == 'POST':
        name = request.POST.get('name')

        if name == "":
            error = "Please Add a Category First !!"
            return render(request,'back/error.html',{'error':error})

        if len(Cat.objects.filter(name=name))!=0:
            error = "This Name Used Before!!"
            return render(request,'back/error.html',{'error':error})

        b = Cat(name=name)
        b.save()
        return redirect ('cat_list')

    return render(request,'back/cat_add.html')


def export_cat_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cat.csv" '

    writer = csv.writer(response)
    writer.writerow(['Title','Counter'])
    for i in Cat.objects.all():

        writer.writerow([i.name,i.count])

    return response

def import_cat_csv(request):

    if request.method == 'POST':
        csv_file = request.FILES['csv_file']  #receiving file

        if not csv_file.name.endswith('.csv'):
            error = "Please Import CSV File!!"
            return render(request,'back/error.html',{'error':error})
        
        if csv_file.multiple_chunks():
            error = "Too Large File!!"
            return render(request,'back/error.html',{'error':error})



        file_data = csv_file.read().decode("utf-8") #turn file into utf
        lines = file_data.split("\n")

        for line in lines :
            fields = line.split(',')  # separate data

            try :

                if len(Cat.objects.filter(name=fields[0])) == 0 and fields[0] != 'Title' and fields[0] != " " :        #saving category into db if not exist
                    b = Cat(name=fields[0])
                    b.save()
                

            except:
                print('finish') 

    return redirect('cat_list')