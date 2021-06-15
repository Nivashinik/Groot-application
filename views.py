import csv,io
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.hashers import make_password, check_password

import datetime
from my_app.models import Contact
# Create your views here.
from django.http import HttpResponse
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
