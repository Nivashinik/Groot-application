import csv,io
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.hashers import make_password, check_password

import datetime
#from my_app.models import formcontact
#from my_app.models import jobcontact
from my_app.models import Contact
# Create your views here.
from django.http import HttpResponse
'''
def index(request):
    return HttpResponse('Hello, World !')
from django.http import HttpResponse
def index1(request):
    return HttpResponse('Hello, World next !')
from django.http import HttpResponse
def index2(request):
     return HttpResponse('I am Nivashini')
from django.http import HttpResponse
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
def template_example1(request):
    # create a dictionary to pass
    # data to the template
    str1={"name":"Kongu", "age":"21" }
   # age1={"age": "21"}
    # return response with template and context
    return render(request, "tem.html", str1)
def registration_example(request):
    # create a dictionary to pass
    # data to the template
   # age1={"age": "21"}
    # return response with template and context
    return render(request, "regis.html")
def template(request):
    str1={"name":"Nivashini K","year":"3rd","interest":"IOT","c":"C and Java","topic":"Smart Streetlight Management System","CGPA":"9.32"}
    return render(request,"current_datetime.html",str1)    
def form(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        print(fname,lname,email,phone)
        ins=formcontact(fname=fname,lname=lname,email=email, phone=phone)
        ins.save()
        print("Data saved sucessfully")
    return render(request, 'home.html')
def jobform(request):
    if request.method=="POST":
        empcode=request.POST['empcode']
        fname=request.POST['fname']
        lname=request.POST['lname']
        jobrole=request.POST['jobrole']
        manager=request.POST['manager']
        print(empcode,fname,lname,jobrole,manager)
        ins1=jobcontact(empcode=empcode,fname=fname,lname=lname,jobrole=jobrole,manager=manager);
        ins1.save()
        print("Data saved sucessfully")
    return render(request, 'job.html')
    
def upload(request):
    if request.method=='POST':
        uploaded_file= request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request,'upload.html')   
    
  '''  


@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    count=0
    template="contact_upload.html"
    prompt={ 
        'order':'Order of the csv should be Name,email,password,message'
        }
    if request.method=="GET":
        return render(request,template,prompt)
        
    csv_file=request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        count=count+1
        _, created = Contact.objects.update_or_create(
            Name=column[0],
            email=column[1],
            password=make_password(column[2]),
            message=column[3],
        )
    print("Records successfully inserted",count)    
    context = {}
    return render(request, template, context)    

    



# Create your views here.
