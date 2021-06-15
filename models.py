from django.db import models
class Contact(models.Model):
    Name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    message=models.TextField()
    
    def _str_(self):
       return f'{self.Name} {self.email}'

     
