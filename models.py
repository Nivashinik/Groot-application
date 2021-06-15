from django.db import models
class formcontact(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    def _str_(self):
       return self.fname
# Create your models here.
class jobcontact(models.Model):
    empcode=models.CharField(max_length=30)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    jobrole=models.CharField(max_length=50)
    manager=models.CharField(max_length=30)
    def _str_(self):
       return self.empcode
class Contact(models.Model):
    Name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    message=models.TextField()
    
    def _str_(self):
       return f'{self.Name} {self.email}'

     