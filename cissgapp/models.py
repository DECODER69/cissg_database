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
    
    
class academic(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')
    school = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    standing = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.serialnumber
    
    
    