from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class extenduser(models.Model):
    
    # firstpart of registration
    firstname = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=30, default='')
    middlename = models.CharField(max_length=30, default='')
    serialnumber = models.CharField(max_length=30, default='')
    birthday = models.CharField(max_length=15, default='')
    division = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=30, default='')
    
    def __str__(self):
        return self.serialnumber
    
    