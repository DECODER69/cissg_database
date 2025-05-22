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
    
    
class other_trainings(models.Model):
    
    serialnumber = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')
    school = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    standing = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.serialnumber

class vocational(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')
    school = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    standing = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.serialnumber
    
    
class coastguard(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')
    authority = models.CharField(max_length=100, default='')
    school = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    standing = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.serialnumber
    
    
class coastguard_local(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')
    authority = models.CharField(max_length=100, default='')
    school = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    standing = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.serialnumber
    
    
class coastguard_foreign(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')
    authority = models.CharField(max_length=100, default='')
    school = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    standing = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.serialnumber
    
    
class military(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')
    authority = models.CharField(max_length=100, default='')
    school = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    standing = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.serialnumber
    
    
class military_local(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')
    authority = models.CharField(max_length=100, default='')
    school = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    standing = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.serialnumber
    
class military_foreign(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')
    authority = models.CharField(max_length=100, default='')
    school = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    standing = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.serialnumber
    
    
class appointments(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')
    date = models.CharField(max_length=100, default='')
    authority = models.CharField(max_length=100, default='')
   
    
    def __str__(self):
        return self.serialnumber
    
    

    
class shipboard(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    unit = models.CharField(max_length=100, default='')
    duty = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    authority = models.CharField(max_length=100, default='')
   
    
    def __str__(self):
        return self.serialnumber
    
    
class collateral(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    unit = models.CharField(max_length=100, default='')
    duty = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    authority = models.CharField(max_length=100, default='')
   
    
    def __str__(self):
        return self.serialnumber
    
class shorebased(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    unit = models.CharField(max_length=100, default='')
    duty = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    authority = models.CharField(max_length=100, default='')
   
    
    def __str__(self):
        return self.serialnumber
    
class collateral2(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    unit = models.CharField(max_length=100, default='')
    duty = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
    authority = models.CharField(max_length=100, default='')
   
    
    def __str__(self):
        return self.serialnumber
    
class government(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    position = models.CharField(max_length=100, default='')
    agency = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')
 
    def __str__(self):
        return self.serialnumber
    
class nongovernment(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    position = models.CharField(max_length=100, default='')
    agency = models.CharField(max_length=100, default='')
    start_date = models.CharField(max_length=20, default='')
    end_date = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.serialnumber
    
    
    # coast guard awards
    
class cgawards(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=100, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    
class cglcommendation(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=500, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    
class cgappreciation(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=500, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    

class cgplaque(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=500, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    
    
    #  afp awards
    
class mawards(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=100, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    
class mlcommendation(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=500, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    
class mappreciation(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=500, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    

class mplaque(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=500, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    
    
    
    # civilian awards
    
    
class clcommendation(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=500, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    
class cappreciation(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=500, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    

class cplaque(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    award = models.CharField(max_length=500, default='')
    authority = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    
    
    
    
    
    
class career(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    student_tour = models.CharField(max_length=100, default='')
    sea_duty = models.CharField(max_length=100, default='')
    staff_duty = models.CharField(max_length=100, default='')
    instructor_duty = models.CharField(max_length=100, default='')
    command = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.serialnumber
    
    
class organization(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    org= models.CharField(max_length=100, default='')
    def __str__(self):
        return self.serialnumber
    
    
class eligibility(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    license= models.CharField(max_length=100, default='')
    def __str__(self):
        return self.serialnumber
    
    
class retirement(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    date= models.CharField(max_length=100, default='')
    def __str__(self):
        return self.serialnumber
    
    
class profile(models.Model):
    serialnumber = models.CharField(max_length=100, default='')
    profile = models.FileField(upload_to='profile_pics/', default='')
    
    def __str__(self):
        return self.serialnumber