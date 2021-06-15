from django.contrib import admin

# Register your models here.
from django.contrib import admin
from my_app.models import formcontact
from my_app.models import jobcontact
from my_app.models import Contact

# Register your models here.
admin.site.register(formcontact)
admin.site.register(jobcontact)
admin.site.register(Contact)
