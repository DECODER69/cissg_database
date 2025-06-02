from django.shortcuts import render

from .models import extenduser, academic, details, other_trainings,vocational, coastguard, coastguard_foreign, coastguard_local, military, military_local, military_foreign, appointments, shipboard, collateral, shorebased, collateral2, government, nongovernment, cgawards, cglcommendation, cgappreciation, cgplaque, mawards, mlcommendation, mappreciation, mplaque, clcommendation, cappreciation, cplaque, career, organization, eligibility, retirement, profile
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
import os
# Create your views here.
def index (request):
     return render(request, 'activities/index.html')


def signup_page(request):
     return render(request, 'activities/signup.html')

def signup (request):
     return render(request, 'activities/signup.html')

def signup_function(request):
     if request.method == 'POST':
          firstname = request.POST.get('firstname')
          middle = request.POST.get('middlename')
          lastname = request.POST.get('lastname')
          serial = request.POST.get('serialnumber')
          birthday = request.POST.get('birthday')
          division = request.POST.get('division')
          password = request.POST.get('password')
          if extenduser.objects.filter(serialnumber=serial).exists():
               print("Serial number already exists")
               messages.error(request, 'ID Number ' + str (serial) + ' Already Exist !')
               return render(request, 'activities/index.html')
          else:
               user = User.objects.create_user(username=serial, password=password, first_name=firstname, last_name=lastname)
               user.save()
               data = extenduser(firstname=firstname, middlename=middle, lastname=lastname, serialnumber=serial, birthday=birthday, division=division, password=password)
               data2 = details(serialnumber=serial, firstname=firstname, middlename=middle, lastname=lastname, birthday=birthday, division=division)
               data2.save()
               data.save()
               return render(request, 'activities/index.html')
          
def login(request):
     details = extenduser.objects.all()
     context = {
          'details': details
     }
     return render(request, 'activities/login.html', context)

def dashboard(request):
     detail2 = details.objects.filter(serialnumber = request.user)
     data = extenduser.objects.filter(serialnumber = request.user)
     user = request.user
     dp = profile.objects.filter(serialnumber = request.user)
   

     context = {
          'data': data,
          'user': user,
          'dp': dp,
          'detail2': detail2,
     }
     
     
     return render(request, 'activities/dashboard.html', context)

def signin_function(request):
     if request.method == "POST":
          username = request.POST["username"]
          password = request.POST["password"]
          birthday = request.POST["birthday"]
          usertype = User.objects.filter(username=username).filter(is_staff=0)
          print (username, password, birthday)
          if User.objects.filter(username=username).exists():
                if usertype:
                    print("gago ka")
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        print("Valid")
                        print(user)
                        return redirect('/dashboard')
                    else:
                        messages.error(request, 'Incorrect password')
                        return redirect('/login')
          else:
               print("Invalid")
               return render(request, 'activities/login.html')
          
          
def  education (request):
     data = extenduser.objects.filter(serialnumber = request.user)
     acad = academic.objects.filter(serialnumber = request.user)
     other = other_trainings.objects.filter(serialnumber = request.user)
     vocation = vocational.objects.filter(serialnumber = request.user)
     user = request.user
     context = {
          'data': data,
          'user': user,
          'acad':acad,
          'other':other,
          'vocation':vocation
     }
     print("data", data)
     return render(request, 'activities/education.html', context)
          
def  education2 (request):
     coastguards = coastguard.objects.filter(serialnumber = request.user)
     local = coastguard_local.objects.filter(serialnumber = request.user)
     foreign = coastguard_foreign.objects.filter(serialnumber = request.user)
     military1 = military.objects.filter(serialnumber = request.user)
     mlocal = military_local.objects.filter(serialnumber = request.user)
     mforeign = military_foreign.objects.filter(serialnumber = request.user)
     user = request.user
     context = {
          'coastguard': coastguards,
          'local': local,
          'foreign': foreign,
          'military': military1,
          'mlocal': mlocal,
          'mforeign': mforeign,
     }
   
     return render(request, 'activities/education2.html', context)




def  education3 (request):
     military1 = military.objects.filter(serialnumber = request.user)
     mlocal = military_local.objects.filter(serialnumber = request.user)
     mforeign = military_foreign.objects.filter(serialnumber = request.user)
     user = request.user
     context = {
          'military': military1,
          'mlocal': mlocal,
          'mforeign': mforeign,
     }
   
     return render(request, 'activities/education3.html', context)
          

     
def delete_item(request, serialnumber):
    extenduser.objects.filter(serialnumber=request.user).delete()
    print(serialnumber)
    return redirect('/dashboard')


def academic_input(request):
     user = request.user
     if request.method == 'POST':
          serialnumber = request.user
          course = request.POST.get('course')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          
          data = academic(serialnumber = request.user,
                          course = course,
                          school = school,
                          start_date = start_date,
                          end_date = end_date,
                          standing = standing)
          data.save()
          
          return redirect('/education')
     
     
     
     
def other_input(request):
     user = request.user
     if request.method == 'POST':
          serialnumber = request.user
          course = request.POST.get('course')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          
          data = other_trainings(serialnumber = request.user,
                                   course = course,
                                   school = school,
                                   start_date = start_date,
                                   end_date = end_date,
                                   standing = standing)
          data.save()
          
          return redirect('/education')
     
     
     
def vocational_input(request):
     user = request.user
     if request.method == 'POST':
          serialnumber = request.user
          course = request.POST.get('course')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          
          data = vocational(serialnumber = request.user,
                                   course = course,
                                   school = school,
                                   start_date = start_date,
                                   end_date = end_date,
                                   standing = standing)
          data.save()
          
          return redirect('/education')
          
def update_table1(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          course = request.POST.get('course')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          academic.objects.filter(id=id).update(course=course,
                                                                    school = school,
                                                                    start_date = start_date,
                                                                    end_date = end_date,
                                                                    standing = standing)

          return redirect('/education')
     print("negative")
     return redirect('/education')


def update_other(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          course = request.POST.get('course')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          other_trainings.objects.filter(id=id).update(course=course,
                                                                    school = school,
                                                                    start_date = start_date,
                                                                    end_date = end_date,
                                                                    standing = standing)

          return redirect('/education')
     print("negative")
     return redirect('/education')



def update_vocational(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          course = request.POST.get('course')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          vocational.objects.filter(id=id).update(course=course,
                                                                    school = school,
                                                                    start_date = start_date,
                                                                    end_date = end_date,
                                                                    standing = standing)

          return redirect('/education')
     print("negative")
     return redirect('/education')




# next page education 2


def coastguard_input(request):
     user = request.user
     if request.method == 'POST':
          serialnumber = request.user
          course = request.POST.get('course')
          authority1 = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          
          data = coastguard(serialnumber = request.user,
                                   course = course, 
                                   authority = authority1,
                                   school = school,
                                   start_date = start_date,
                                   end_date = end_date,
                                   standing = standing)
          data.save()
          
          return redirect('/education2')
     
def cglocal_input(request):
     user = request.user
     if request.method == 'POST':
          serialnumber = request.user
          course = request.POST.get('course')
          authority1 = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          
          data = coastguard_local(serialnumber = request.user,
                                   course = course, 
                                   authority = authority1,
                                   school = school,
                                   start_date = start_date,
                                   end_date = end_date,
                                   standing = standing)
          data.save()
          
          return redirect('/education2')
     
     
     
def cgforeign_input(request):
     user = request.user
     if request.method == 'POST':
          serialnumber = request.user
          course = request.POST.get('course')
          authority1 = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          
          data = coastguard_foreign(serialnumber = request.user,
                                   course = course, 
                                   authority = authority1,
                                   school = school,
                                   start_date = start_date,
                                   end_date = end_date,
                                   standing = standing)
          data.save()
          
          return redirect('/education2')
     
     
     
     # SECOND PAGE EDUCATION 2 EDIT TABLE
     
     
def update_coastguard(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          course = request.POST.get('course')
          authority = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          coastguard.objects.filter(id=id).update(course=course, authority=authority,
                                                                 school = school,
                                                                 start_date = start_date,
                                                                 end_date = end_date,
                                                                 standing = standing)

          return redirect('/education2')
     print("negative")
     return redirect('/education2')



def update_cglocal(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          course = request.POST.get('course')
          authority = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          coastguard_local.objects.filter(id=id).update(course=course, authority=authority,
                                                                 school = school,
                                                                 start_date = start_date,
                                                                 end_date = end_date,
                                                                 standing = standing)

          return redirect('/education2')
     print("negative")
     return redirect('/education2')

def update_cgforeign(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          course = request.POST.get('course')
          authority = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          coastguard_foreign.objects.filter(id=id).update(course=course, authority=authority,
                                                                 school = school,
                                                                 start_date = start_date,
                                                                 end_date = end_date,
                                                                 standing = standing)

          return redirect('/education2')
     print("negative")
     return redirect('/education2')





          #   EDUCATION 3
          
def military_input(request):
     user = request.user
     if request.method == 'POST':
          serialnumber = request.user
          course = request.POST.get('course')
          authority1 = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          
          data = military(serialnumber = request.user,
                                   course = course, 
                                   authority = authority1,
                                   school = school,
                                   start_date = start_date,
                                   end_date = end_date,
                                   standing = standing)
          data.save()
          
          return redirect('/education3')
     
def mlocal_input(request):
     user = request.user
     if request.method == 'POST':
          serialnumber = request.user
          course = request.POST.get('course')
          authority1 = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          
          data = military_local(serialnumber = request.user,
                                   course = course, 
                                   authority = authority1,
                                   school = school,
                                   start_date = start_date,
                                   end_date = end_date,
                                   standing = standing)
          data.save()
          
          return redirect('/education3')
     
     
     
def mforeign_input(request):
     user = request.user
     if request.method == 'POST':
          serialnumber = request.user
          course = request.POST.get('course')
          authority1 = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          
          data = military_foreign(serialnumber = request.user,
                                   course = course, 
                                   authority = authority1,
                                   school = school,
                                   start_date = start_date,
                                   end_date = end_date,
                                   standing = standing)
          data.save()
          
          return redirect('/education3')
     
     
     
     
     # UPDATE EDUCATION 3
     
     
     

def update_military(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          course = request.POST.get('course')
          authority = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          military.objects.filter(id=id).update(course=course, authority=authority,
                                                                 school = school,
                                                                 start_date = start_date,
                                                                 end_date = end_date,
                                                                 standing = standing)

          return redirect('/education3')
     print("negative")
     return redirect('/education3')



def update_mlocal(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          course = request.POST.get('course')
          authority = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          military_local.objects.filter(id=id).update(course=course, authority=authority,
                                                                 school = school,
                                                                 start_date = start_date,
                                                                 end_date = end_date,
                                                                 standing = standing)

          return redirect('/education3')
     print("negative")
     return redirect('/education3')

def update_mforeign(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          course = request.POST.get('course')
          authority = request.POST.get('authority')
          school = request.POST.get('school')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          standing = request.POST.get('standing')
          military_foreign.objects.filter(id=id).update(course=course, authority=authority,
                                                                 school = school,
                                                                 start_date = start_date,
                                                                 end_date = end_date,
                                                                 standing = standing)

          return redirect('/education3')
     print("negative")
     return redirect('/education3')




#     END OF UODATE EDUCATION 3





               #  APPOINTMENTS
               
               
def education4(request):
     appointment = appointments.objects.filter(serialnumber = request.user)
     context = {
          'appointment': appointment,
     }
     return render(request, 'activities/education4.html', context)

def appointment_input(request):
     if request.method == 'POST':
          des = request.POST.get('description')
          date = request.POST.get('date')
          authority = request.POST.get('authority')
          
          data = appointments(serialnumber = request.user,
               description=des, date=date, authority=authority
               
          )
          
          data.save()
          return redirect('/education4')
     
     

def appointment_update(request, id):
     if request.method == 'POST':
          des = request.POST.get('description')
          date = request.POST.get('date')
          authority = request.POST.get('authority')
          
          appointments.objects.filter(id=id).update(
               description=des, date=date, authority=authority)
         
          return redirect('/education4')



def education5(request):
     shipboards = shipboard.objects.filter(serialnumber = request.user)
     collateral1 = collateral.objects.filter(serialnumber = request.user)
     shorebased1 = shorebased.objects.filter(serialnumber = request.user)
     collateral1a = collateral2.objects.filter(serialnumber = request.user)
     government1 = government.objects.filter(serialnumber = request.user)
     nongovernment1 = nongovernment.objects.filter(serialnumber = request.user)
     context = {
          'shipboard': shipboards,
          'collateral': collateral1,
          'shorebased': shorebased1,
          'collateral2': collateral1a,
          'government': government1,
          'nongovernment': nongovernment1,
     }
     return render(request, 'activities/education5.html', context)




# G. DUTY ASSIGNMENTS AND ADDITIONAL DUTIES:

def shipboard_input(request):
     if request.method == 'POST':
          unit = request.POST.get('unit')
          position = request.POST.get('position')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          authority = request.POST.get('authority')
          
          data = shipboard(serialnumber = request.user,
                                   unit = unit, 
                                   duty = position,
                                   start_date = start_date,
                                   end_date = end_date,
                                   authority = authority)
          data.save()
          
          return redirect('/education5')
     
     
def collateral_input(request):
     if request.method == 'POST':
          unit = request.POST.get('unit')
          position = request.POST.get('position')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          authority = request.POST.get('authority')
          
          data = collateral(serialnumber = request.user,
                                   unit = unit, 
                                   duty = position,
                                   start_date = start_date,
                                   end_date = end_date,
                                   authority = authority)
          data.save()
          
          return redirect('/education5')
     
     
def update_shipboard(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          unit = request.POST.get('unit')
          position = request.POST.get('duty')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          authority = request.POST.get('authority')
          shipboard.objects.filter(id=id).update(unit=unit, duty=position,
                                                                 start_date = start_date,
                                                                 end_date = end_date,
                                                                 authority = authority)

          return redirect('/education5')
     print("negative")
     return redirect('/education5')

def update_collateral(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          unit = request.POST.get('unit')
          position = request.POST.get('duty')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          authority = request.POST.get('authority')
          collateral.objects.filter(id=id).update(unit=unit, duty=position,
                                                                 start_date = start_date,
                                                                 end_date = end_date,
                                                                 authority = authority)

          return redirect('/education5')
     print("negative")
     return redirect('/education5')





# 2.	SHORE BASED:


def education6(request):
     shorebased1 = shorebased.objects.filter(serialnumber = request.user)
     collateral1a = collateral2.objects.filter(serialnumber = request.user)
     context = {
          'shorebased': shorebased1,
          'collateral2': collateral1a,
     }
     return render(request, 'activities/education6.html', context)



def shorebased_input(request):
     if request.method == 'POST':
          unit = request.POST.get('unit')
          position = request.POST.get('position')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          authority = request.POST.get('authority')
          
          data = shorebased(serialnumber = request.user,
                                   unit = unit, 
                                   duty = position,
                                   start_date = start_date,
                                   end_date = end_date,
                                   authority = authority)
          data.save()
          
          return redirect('/education6')
     
     
def collateral2_input(request):
     if request.method == 'POST':
          unit = request.POST.get('unit')
          position = request.POST.get('position')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          authority = request.POST.get('authority')
          
          data = collateral2(serialnumber = request.user,
                                   unit = unit, 
                                   duty = position,
                                   start_date = start_date,
                                   end_date = end_date,
                                   authority = authority)
          data.save()
          
          return redirect('/education6')
     
     
def update_shorebased(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          unit = request.POST.get('unit')
          position = request.POST.get('duty')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          authority = request.POST.get('authority')
          shorebased.objects.filter(id=id).update(unit=unit, duty=position,
                                                                 start_date = start_date,
                                                                 end_date = end_date,
                                                                 authority = authority)

          return redirect('/education6')
     print("negative")
     return redirect('/education6')

def update_collateral2(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          unit = request.POST.get('unit')
          position = request.POST.get('duty')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          authority = request.POST.get('authority')
          collateral2.objects.filter(id=id).update(unit=unit, duty=position,
                                                                 start_date = start_date,
                                                                 end_date = end_date,
                                                                 authority = authority)

          return redirect('/education6')
     print("negative")
     return redirect('/education6')



# OTHERS: a. Other Government Service

def education7(request):
     gov = government.objects.filter(serialnumber = request.user)
     nongov = nongovernment.objects.filter(serialnumber = request.user)
     context = {
          'gov': gov,
          'nongov': nongov,
     }
     return render(request, 'activities/education7.html', context)



def gov_input(request):
     if request.method == 'POST':
          positions = request.POST.get('position')
          agencies = request.POST.get('agency')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
         
          
          data = government(serialnumber = request.user,
                                   position = positions, 
                                   agency = agencies,
                                   start_date = start_date,
                                   end_date = end_date)
          data.save()
          
          return redirect('/education7')
     
     
def nongov_input(request):
     if request.method == 'POST':
          positions = request.POST.get('position')
          agencies = request.POST.get('agency')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
         
          
          data = nongovernment(serialnumber = request.user,
                                   position = positions, 
                                   agency = agencies,
                                   start_date = start_date,
                                   end_date = end_date)
          data.save()
          
          return redirect('/education7')
     
     
def update_gov(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          positions = request.POST.get('position')
          agencies = request.POST.get('agency')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          government.objects.filter(id=id).update(position=positions, agency=agencies,
                                                                 start_date = start_date,
                                                                 end_date = end_date)

          return redirect('/education7')
     print("negative")
     return redirect('/education7')

def update_nongov(request, id):
     user = request.user
     print(user)
     if request.method == 'POST':
          positions = request.POST.get('position')
          agencies = request.POST.get('agency')
          start_date = request.POST.get('start_date')
          end_date = request.POST.get('end_date')
          nongovernment.objects.filter(id=id).update(position=positions, agency=agencies,
                                                                 start_date = start_date,
                                                                 end_date = end_date)

          return redirect('/education7')
     print("negative")
     return redirect('/education7')




# H. AWARDS AND RECOGNITIONS:



def education8(request):
     awards = cgawards.objects.filter(serialnumber = request.user)
     commendations = cglcommendation.objects.filter(serialnumber = request.user)
     appreciations = cgappreciation.objects.filter(serialnumber = request.user)
     plaque = cgplaque.objects.filter(serialnumber = request.user)
     context = {
          'awards': awards,
          'commendations': commendations,
          'appreciations': appreciations,
          'plaque':plaque,
     }
     return render(request, 'activities/education8.html', context)




def award_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = cgawards(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education8')
     
def commendation_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = cglcommendation(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education8')
     
def appreciation_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = cgappreciation(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education8')
     
def plaque_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = cgplaque(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education8')
     
     
def update_award(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          cgawards.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education8')
     print("negative")
     return redirect('/education8')

def update_commendation(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          cglcommendation.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education8')
     print("negative")
     return redirect('/education8')

def update_appreciation(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          cgappreciation.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education8')
     print("negative")
     return redirect('/education8')

def update_plaque(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          cgplaque.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education8')
     print("negative")
     return redirect('/education8')





          # 2. Military (AFP)
          
def education9(request):
     awards = mawards.objects.filter(serialnumber = request.user)
     commendations = mlcommendation.objects.filter(serialnumber = request.user)
     appreciations = mappreciation.objects.filter(serialnumber = request.user)
     plaque = mplaque.objects.filter(serialnumber = request.user)
     context = {
          'awards': awards,
          'commendations': commendations,
          'appreciations': appreciations,
          'plaque':plaque,
     }
     return render(request, 'activities/education9.html', context)



def maward_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = mawards(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education9')
     
def mcommendation_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = mlcommendation(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education9')
     
def mappreciation_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = mappreciation(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education9')
     
def mplaque_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = mplaque(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education9')
     
     
def update_maward(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          mawards.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education9')
     print("negative")
     return redirect('/education9')

def update_mcommendation(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          mlcommendation.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education9')
     print("negative")
     return redirect('/education9')

def update_mappreciation(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          mappreciation.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education9')
     print("negative")
     return redirect('/education9')

def update_mplaque(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          mplaque.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education9')
     print("negative")
     return redirect('/education9')



          # 3. Civilian (Commendations/Appreciations/Plaque)
          
def education10(request):
     commendations = clcommendation.objects.filter(serialnumber = request.user)
     appreciations = cappreciation.objects.filter(serialnumber = request.user)
     plaque = cplaque.objects.filter(serialnumber = request.user)
     context = {
          'commendations': commendations,
          'appreciations': appreciations,
          'plaque':plaque,
     }
     return render(request, 'activities/education10.html', context)



def ccommendation_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = clcommendation(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education10')
     
     
def cappreciation_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = cappreciation(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education10')
     
def cplaque_input(request):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          data = cplaque(serialnumber = request.user,
                                   award = awards, 
                                   authority = auth)
          data.save()
          return redirect('/education10')
     
     # UPDATE

def update_ccommendation(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          clcommendation.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education10')
     print("negative")
     return redirect('/education10')
     
def update_cappreciation(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          cappreciation.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education10')
     print("negative")
     return redirect('/education10')

def update_cplaque(request, id):
     if request.method == 'POST':
          awards = request.POST.get('awards')
          auth = request.POST.get('auth')
          cplaque.objects.filter(id=id).update(award=awards, authority=auth)

          return redirect('/education10')
     print("negative")
     return redirect('/education10')


def education11(request):
     careers = career.objects.filter(serialnumber = request.user)
     
     
     context = {
          'careers': careers,
          
     }
     return render(request, 'activities/education11.html', context)





def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        if image:
            try:
                # Check if profile already exists
                existing_profile = profile.objects.get(serialnumber=request.user)

                # Delete old image file....
                if existing_profile.profile:
                    old_image_path = existing_profile.profile.path
                    if os.path.isfile(old_image_path):
                        os.remove(old_image_path)

                # Update with new image inseerrtttt
                existing_profile.profile = image
                existing_profile.save()

            except profile.DoesNotExist:
                # Create new profile if it doesn't exist
                new_profile = profile(serialnumber=request.user, profile=image)
                new_profile.save()

        return redirect('/education11')


def career_input(request):

     if request.method == 'POST':
          student = request.POST.get('student')
          sea = request.POST.get('sea')
          staff = request.POST.get('staff')
          instructor = request.POST.get('instructor')
          command = request.POST.get('command')

          # Try to get existing record
          data, created = career.objects.update_or_create(
               serialnumber=request.user,
               defaults={
                    'student_tour': student,
                    'sea_duty': sea,
                    'staff_duty': staff,
                    'instructor_duty': instructor,
                    'command': command
               }
          )

          return redirect('/education11')
     
     
     
     
     
     
     
                                   #  DASHBOARD FUNCTIONS
                                   
                                   
def dashboard_input(request):
     if request.method == 'POST':
          lastname = request.POST.get('lastname')
          firstname = request.POST.get('firstname')
          middlename = request.POST.get('middlename')
         
          birthday = request.POST.get('birthdate')
          birthplace = request.POST.get('birthplace')
          nickname = request.POST.get('nickname')
          gender = request.POST.get('gender')
          religion = request.POST.get('religion')
          height = request.POST.get('height')
          headsize = request.POST.get('headsize')
          waistsize = request.POST.get('waistsize')
          skincolor = request.POST.get('skincolor')
          distinct = request.POST.get('distinct')
          civilstatus = request.POST.get('civilstatus')
          citizenship = request.POST.get('citizenship')
          bloodtype = request.POST.get('bloodtype')
          weight = request.POST.get('weight')
          footsize = request.POST.get('footsize')
          bodybuild = request.POST.get('bodybuild')
          eyecolor = request.POST.get('eyecolor')
          haircolor = request.POST.get('haircolor')
          homeaddress = request.POST.get('homeaddress')
          permanentaddress = request.POST.get('permanentaddress')
          email = request.POST.get('email')
          contactnumber = request.POST.get('contactnumber')
          pagibig = request.POST.get('pagibig')
          philhealth = request.POST.get('philhealth')
          sssnumber  = request.POST.get('sssnumber')
          gsis = request.POST.get('gsis')
          tin = request.POST.get('tin')
          driver = request.POST.get('driver')
          rank = request.POST.get('rank')
          data = details(serialnumber = request.user,
                         lastname = lastname,
                         firstname = firstname,
                         middlename = middlename,
                         birthday = birthday,
                         birthplace = birthplace,
                         nickname = nickname,
                         gender = gender, 
                         religion = religion,
                         height = height,
                         headsize = headsize,
                         waistsize = waistsize,
                         skincolor = skincolor,
                         distinct = distinct,
                         civilstatus = civilstatus,
                         citizenship = citizenship,
                         bloodtype = bloodtype,
                         weight = weight,
                         footsize = footsize,
                         bodybuild = bodybuild,
                         eyecolor = eyecolor,
                         haircolor = haircolor,
                         homeaddress = homeaddress,
                         permanentaddress = permanentaddress,
                         email = email,
                         contactnumber = contactnumber,
                         pagibig = pagibig,
                         philhealth = philhealth,
                         sssnumber = sssnumber,
                         gsis = gsis,
                         tin = tin,
                         driver = driver,
                         rank = rank)
          data.save()
          
          return redirect('/dashboard')
     
     
def dashboard_input_update(request, id):
     if request.method == 'POST':
          lastname = request.POST.get('lastname')
          firstname = request.POST.get('firstname')
          middlename = request.POST.get('middlename')
          
          birthday = request.POST.get('birthdate')
          birthplace = request.POST.get('birthplace')
          nickname = request.POST.get('nickname')
          gender = request.POST.get('gender')
          religion = request.POST.get('religion')
          height = request.POST.get('height')
          headsize = request.POST.get('headsize')
          waistsize = request.POST.get('waistsize')
          skincolor = request.POST.get('skincolor')
          distinct = request.POST.get('distinct')
          civilstatus = request.POST.get('civilstatus')
          citizenship = request.POST.get('citizenship')
          bloodtype = request.POST.get('bloodtype')
          weight = request.POST.get('weight')
          footsize = request.POST.get('footsize')
          bodybuild = request.POST.get('bodybuild')
          eyecolor = request.POST.get('eyecolor')
          haircolor = request.POST.get('haircolor')
          homeaddress = request.POST.get('homeaddress')
          permanentaddress = request.POST.get('permanentaddress')
          email = request.POST.get('email')
          contactnumber = request.POST.get('contactnumber')
          pagibig = request.POST.get('pagibig')
          philhealth = request.POST.get('philhealth')
          sssnumber  = request.POST.get('sssnumber')
          gsis = request.POST.get('gsis')
          tin = request.POST.get('tin')
          driver = request.POST.get('driver')
          rank = request.POST.get('rank')
          details.objects.filter(id=id).update(lastname = lastname,
                         firstname = firstname,
                         middlename = middlename,
                         birthday = birthday,
                         birthplace = birthplace,
                         nickname = nickname,
                         gender = gender, 
                         religion = religion,
                         height = height,
                         headsize = headsize,
                         waistsize = waistsize,
                         skincolor = skincolor,
                         distinct = distinct,
                         civilstatus = civilstatus,
                         citizenship = citizenship,
                         bloodtype = bloodtype,
                         weight = weight,
                         footsize = footsize,
                         bodybuild = bodybuild,
                         eyecolor = eyecolor,
                         haircolor = haircolor,
                         homeaddress = homeaddress,
                         permanentaddress = permanentaddress,
                         email = email,
                         contactnumber = contactnumber,
                         pagibig = pagibig,
                         philhealth = philhealth,
                         sssnumber = sssnumber,
                         gsis = gsis,
                         tin = tin,
                         driver = driver,
                         rank = rank)
          # data.save()
          
          return redirect('/dashboard')