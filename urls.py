"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from my_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="homepage"),
    path('next/',views.index1, name="homepage"),
    path('final/',views.index2, name="homepage"),
    path('dateandtime/',views.current_datetime),
    url(r'^time/plus/(\d+)/$', views.hours_ahead, name='hours_ahead'),
    path('template_example1/',views.template_example1),    
    path('registration/',views.registration_example),
    path('template/',views.template),
    path('home/', views.form, name='form'),
    path('job/',views.jobform,name='jobform'),
    path('upload/',views.upload,name='upload'),
    path('upload-csv/',views.contact_upload, name="contact_upload"),
]
