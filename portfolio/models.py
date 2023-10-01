from django.db import models

# Create your models here.
class Port_Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    message=models.TextField()

    def __str__(self):
        return self.name
    

    