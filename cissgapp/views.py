from django.shortcuts import render

from .models import extenduser, record, leaves, academic, details, dependents, triple, other_trainings,vocational, coastguard, coastguard_foreign, coastguard_local, military, military_local, military_foreign, appointments, shipboard, collateral, shorebased, collateral2, government, nongovernment, cgawards, cglcommendation, cgappreciation, cgplaque, mawards, mlcommendation, mappreciation, mplaque, clcommendation, cappreciation, cplaque, career, organization, eligibility, retirement, profile
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
import os
from django.contrib.auth.decorators import login_required
from datetime import date
from django.utils import timezone
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa


# Create your views here.
def index (request):
     return render(request, 'activities/index.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

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

        # if ID exists
        if extenduser.objects.filter(serialnumber=serial).exists():
            messages.error(request, f'ID Number {serial} already exists!')
            # Send back the data so form can refill
            return render(request, 'activities/index.html', {
                'form_data': request.POST
            })

        # else create
        user = User.objects.create_user(
            username=serial, password=password,
            first_name=firstname, last_name=lastname
        )
        user.save()

        data = extenduser(
            firstname=firstname, middlename=middle, lastname=lastname,
            serialnumber=serial, birthday=birthday,
            division=division, password=password
        )
        data.save()

        data2 = details(
            serialnumber=serial, firstname=firstname, middlename=middle,
            lastname=lastname, birthday=birthday, division=division
        )
        data2.save()

        messages.success(request, 'Account created successfully! Please login.')
        return render(request, 'activities/index.html')

    return render(request, 'activities/index.html')
          
def login(request):
     details = extenduser.objects.all()
     context = {
          'details': details
     }
     return render(request, 'activities/login.html', context)
@login_required(login_url='/login')
def dashboard(request):
     depend = dependents.objects.filter(serialnumber = request.user)
     detail2 = details.objects.filter(serialnumber = request.user)
     data = extenduser.objects.filter(serialnumber = request.user)
     user = request.user
     dp = details.objects.filter(serialnumber = request.user)
   

     context = {
          'data': data,
          'user': user,
          'dp': dp,
          'detail2': detail2,
          'depend': depend,
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
     dp = details.objects.filter(serialnumber = request.user)
     user = request.user
     context = {
          'data': data,
          'user': user,
          'acad':acad,
          'other':other,
          'vocation':vocation,
          'dp': dp,
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
     dp = details.objects.filter(serialnumber = request.user)
     context = {
          'coastguard': coastguards,
          'local': local,
          'foreign': foreign,
          'military': military1,
          'mlocal': mlocal,
          'mforeign': mforeign,
          'user': user,
          'dp': dp,
     }
   
     return render(request, 'activities/education2.html', context)




def  education3 (request):
     military1 = military.objects.filter(serialnumber = request.user)
     mlocal = military_local.objects.filter(serialnumber = request.user)
     mforeign = military_foreign.objects.filter(serialnumber = request.user)
     user = request.user
     dp = details.objects.filter(serialnumber = request.user)
     context = {
          'military': military1,
          'mlocal': mlocal,
          'mforeign': mforeign,
          'user': user,
          'dp': dp,
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
     dp = details.objects.filter(serialnumber = request.user)
     context = {
          'appointment': appointment,
          'dp': dp,
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
     dp = details.objects.filter(serialnumber = request.user)
     context = {
          'shipboard': shipboards,
          'collateral': collateral1,
          'shorebased': shorebased1,
          'collateral2': collateral1a,
          'government': government1,
          'nongovernment': nongovernment1,
          'dp': dp,
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
     dp = details.objects.filter(serialnumber = request.user)
     context = {
          'shorebased': shorebased1,
          'collateral2': collateral1a,
          'dp': dp,
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
     dp = details.objects.filter(serialnumber = request.user)
     context = {
          'gov': gov,
          'nongov': nongov,
          'dp': dp,
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
     dp = details.objects.filter(serialnumber = request.user)
     context = {
          'awards': awards,
          'commendations': commendations,
          'appreciations': appreciations,
          'plaque':plaque,
          'dp': dp,
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
     dp = details.objects.filter(serialnumber = request.user)
     context = {
          'awards': awards,
          'commendations': commendations,
          'appreciations': appreciations,
          'plaque':plaque,
          'dp': dp,
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
     dp = details.objects.filter(serialnumber = request.user)
     context = {
          'commendations': commendations,
          'appreciations': appreciations,
          'plaque':plaque,
          'dp': dp,
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
     data = extenduser.objects.filter(serialnumber = request.user)
     dp = details.objects.filter(serialnumber = request.user)
     triples = triple.objects.filter(serialnumber = request.user)
    
     
     
     context = {
          'careers': careers,
          'data': data,
          'dp':dp,
          'triples': triples,
          
          
     }
     return render(request, 'activities/education11.html', context)





def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        if image:
            try:
                # Check if record exists for this user
                existing_profile = details.objects.get(serialnumber=request.user.username)  # or use request.user.id if applicable

                # Delete old image if exists
                if existing_profile.profile and os.path.isfile(existing_profile.profile.path):
                    os.remove(existing_profile.profile.path)

                # Update image
                existing_profile.profile = image
                existing_profile.save()

            except details.DoesNotExist:
                # Create new record if none exists
                new_profile = details(
                    serialnumber=request.user.username,  # or use request.user.id
                    profile=image
                )
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
     
     
def triple_input(request):
    
     if request.method == 'POST':
          org = request.POST.get('org')
          license = request.POST.get('license')
          date = request.POST.get('date')

          # Try to get existing record
          data, created = triple.objects.update_or_create(
               serialnumber=request.user,
               defaults={
                    'org': org,
                    'license': license,
                    'date': date,
                    
               }
          )

          return redirect('/education11')
     
     
     
     
                                   #  DASHBOARD FUNCTIONS
                                   
                                   
def dashboard_input(request):
     if request.method == 'POST':
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
          details.objects.filter(id=id).update(birthday = birthday,
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
     
     

def dependents_input(request):

     if request.method == 'POST':
          name = request.POST.get('name')
          relationship = request.POST.get('relationship')
          birthday = request.POST.get('birthday')
          

          # Try to get existing record
          data = dependents(serialnumber=request.user, 
                            name=name, 
                            relationship=relationship, 
                            birthday=birthday
          )
          data.save()

          return redirect('/dashboard')
     
     
def update_dependents(request, id):
     if request.method == 'POST':
          name = request.POST.get('name')
          relationship = request.POST.get('relationship')
          birthday = request.POST.get('birthday')
          dependents.objects.filter(id=id).update(name=name, relationship=relationship, birthday=birthday)

          return redirect('/dashboard')
     
     return redirect('/dashboard')
     
     
     
     
     
     
     # ADMIN PART
     



# def triple(request):
#      if request.method == 'POST':
#           org  = request.POST.get('organization')
#           elig= request.POST.get('eligibility')
#           retire = request.POST.get('compulsory')
         
          
#           return redirect('/education11')
     
#      if request.method == 'POST':
#           org  = request.POST.get('organization')
#           elig= request.POST.get('eligibility')
#           retire = request.POST.get('compulsory')

#                # Try to get existing record
#           data, created = organization.objects.update_or_create(
#                     serialnumber=request.user,
#                     defaults={
#                          'org': org,
#                     }
#                )
          
#           data, created = eligibility.objects.update_or_create(
#                     serialnumber=request.user,
#                     defaults={
#                          'license': elig,
#                     }
#                )
          
#           data, created = retirement.objects.update_or_create(
#                     serialnumber=request.user,
#                     defaults={
#                          'date': retire,
#                     }
#                )

#           return redirect('/education11')
     
      
from datetime import date

from datetime import date, datetime

from datetime import date, datetime
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Count, Q

def admin_dashboard(request):
    today = date.today()
    

    # All defined leave types
    leave = leaves.objects.all()

    # Personnel currently on leave (exclude Duty/empty/null)
    personnels = details.objects.filter(
        leave_start__lte=today
    ).exclude(
        Q(status='Duty') | Q(status__isnull=True) | Q(status='')
    )

    # Personnel currently on duty
    duty = details.objects.filter(
        Q(status='Duty') | Q(leave_start__gt=today)
    ).count()

    # Get all defined leave type names (strings)
    leave_types = leaves.objects.values_list('leave', flat=True)

    # Count how many personnel per leave type
    leave_counts = (
        details.objects
        .filter(status__in=leave_types, leave_start__lte=today)
        .values('status')
        .annotate(count=Count('id', distinct=True))
    )
    # Example: [{'status': 'Sick Leave', 'count': 5}, {'status': 'R&R', 'count': 3}]
    leave_count_dict = {item['status']: item['count'] for item in leave_counts}

    # Combine leave types with counts
    leave_data = [
        {
            'leave': l.leave,
            'count': leave_count_dict.get(l.leave, 0)
        }
        for l in leave
    ]

    # Paginate personnels
    paginator = Paginator(personnels, 10)
    page_number = request.GET.get('page')
    personnels = paginator.get_page(page_number)
    today = date.today()
    context = {
        'duty': duty,
        'personnels': personnels,
        'leave_data': leave_data, 
        'leave':leave,
        'today': today,
    }
    return render(request, 'activities/admindashboard.html', context)



def add_personnel(request):
     person = details.objects.all()
     leave = leaves.objects.all()
     
     context = {
          'person': person,
          'leave': leave,
     }
    
     
     return render(request, 'activities/addpers.html', context)


def add_status(request):
    if request.method == 'POST':
        serial = request.POST.get('serial')
        leave = request.POST.get('leave')
        address = request.POST.get('address')
        order = request.POST.get('order')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        fullname = request.POST.get('fullname')
        
        print(fullname)
        
        data1 = record(serialnumber=serial,
                       fullname=fullname, leave=leave,
                       address=address, startdate=startdate,
                       enddate=enddate, order=order)
        data1.save()

        # Convert to date object
        try:
            start_date_obj = datetime.strptime(startdate, '%Y-%m-%d').date()
            end_date_obj = datetime.strptime(enddate, '%Y-%m-%d').date()
        except ValueError as e:
            print("Date format error:", e)
            return redirect('/admin_dashboard')

        today = timezone.now().date()

        # Automatically update status if leave starts today or earlier
        status = leave
        if start_date_obj <= today <= end_date_obj:
            status = leave

        try:
            data, created = details.objects.update_or_create(
                serialnumber=serial,
                defaults={
                    'status': status,
                    'leave_start': start_date_obj,
                    'leave_end': end_date_obj,
                }
            )
        except Exception as e:
            print("Error saving to DB:", e)

        return redirect('/admin_dashboard')
    
from django.db import transaction
from django.shortcuts import redirect
from django.contrib import messages
from .models import details, record

def update_status(request):
    if request.method == 'POST':
        serialnumber = request.POST.get('serialnumber')
        status = request.POST.get('status')

        try:
            with transaction.atomic():
                # ✅ Update all matching details rows
                details_updated = details.objects.filter(serialnumber=serialnumber)
                if details_updated.exists():
                    details_updated.update(status=status)
                else:
                    messages.error(request, "Personnel not found.")
                    return redirect('/admin_dashboard')

                # ✅ Update all matching record rows (if they exist)
                record.objects.filter(serialnumber=serialnumber).update(status=status)

                # Optional: If you want to display name of first personnel
                first_person = details_updated.first()
                messages.success(
                    request,
                    f"Status for {first_person.firstname} {first_person.lastname} updated successfully."
                )

        except Exception as e:
            messages.error(request, f"Error updating status: {e}")

    return redirect('/admin_dashboard')




from django.utils import timezone
from datetime import datetime
from .models import details

from django.utils import timezone
from datetime import datetime

def cissg_personnel(request):
    LEAVE_STATUSES = leaves.objects.values_list('leave', flat=True)
    today = timezone.now().date()

    # Count personnel with status = 'Duty'
    present = details.objects.filter(status='Duty').count()

    # Count those with leave-related status and whose leave_start has started
    on_leave = details.objects.filter(
        status__in=LEAVE_STATUSES,
        leave_start__lte=today
    ).count()

    total = present + on_leave

    percent_duty = int((present / total) * 100) if total > 0 else 0

    personnels = details.objects.all()

    for p in personnels:
        leave_start = p.leave_start

        if isinstance(leave_start, str):
            try:
                leave_start = datetime.strptime(leave_start, '%Y-%m-%d').date()
            except ValueError:
                leave_start = None

        # Dynamically assign display_status
        if p.status in LEAVE_STATUSES and leave_start and today < leave_start:
            p.display_status = "Duty"
        else:
            p.display_status = p.status

    context = {
        'personnels': personnels,
        'present': present,
        'on_leave': on_leave,
        'percent_duty': percent_duty,
        'total': total
    }

    return render(request, 'activities/pers.html', context)



def view_personnel(request, serial):
    person = get_object_or_404(details, serialnumber=serial)
    
    context = {
         'person':person,
    }
    print(person)
    
    return render(request, 'activities/view.html', context)


def personnel_profile(request):
     return render(request, 'activities/view.html')


# derletes


def delete_academic(request, id):
    academic.objects.filter(id=id).delete()
    print("Academic record deleted for:", id)
    return redirect('/education')

def delete_vocational(request, id):
    vocational.objects.filter(id=id).delete()
    print("Academic record deleted for:", id)
    return redirect('/education')

def delete_other(request, id):
    other_trainings.objects.filter(id=id).delete()
    print("Academic record deleted for:", id)
    return redirect('/education')


def delete_coastguard(request, id):
    coastguard.objects.filter(id=id).delete()
    print("Coast Guard record deleted for:", id)
    return redirect('/education2')

def delete_local(request, id):
    coastguard_local.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education2')

def delete_foreign(request, id):
    coastguard_foreign.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education2')

def delete_military(request, id):
    military.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education3')


def delete_mlocal(request, id):
    military_local.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education3')

def delete_mforeign(request, id):
    military_foreign.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education3')


def delete_appointment(request, id):
    appointments.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education4')

def delete_shipboard(request, id):
    shipboard.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education5')

def delete_collateral(request, id):
    collateral.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education5')

def delete_shorebased(request, id):
    shorebased.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education6')

def delete_collateral2(request, id):
    collateral2.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education6')


def delete_government(request, id):
    government.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education7')

def delete_nongovernment(request, id):
    nongovernment.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education7')


def delete_awards(request, id):
    cgawards.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education8')


def delete_commendation(request, id):
    cglcommendation.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education8')

def delete_appreciation(request, id):
    cgappreciation.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education8')

def delete_plaque(request, id):
    cgplaque.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education8')




def delete_mawards(request, id):
    mawards.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education9')


def delete_mcommendation(request, id):
    mlcommendation.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education9')

def delete_mappreciation(request, id):
    mappreciation.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education9')

def delete_mplaque(request, id):
    mplaque.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education9')



def delete_ccommendation(request, id):
    clcommendation.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education10')

def delete_cappreciation(request, id):
    cappreciation.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education10')

def delete_cplaque(request, id):
    cplaque.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/education10')


def delete_dependents(request, id):
    dependents.objects.filter(id=id).delete()
    print("Local record deleted for:", id)
    return redirect('/dashboard')





# generate PDF



from datetime import date
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.db.models import Q
from .models import details

def generate_personnel_pdf(request):
    today = date.today()
    now = datetime.now()
    timestamp = now.strftime("%d %b %Y %I:%M %p")

    # ✅ Dynamic statuses from database + Duty
    leave_statuses = list(
        leaves.objects.values_list('leave', flat=True)
    )
    statuses = leave_statuses + ['Duty']

    leave_data = []
    total_strength = 0

    for s in statuses:
        if s == "Duty":
            count = details.objects.filter(
                Q(status='Duty') |
                Q(leave_start__gt=today) |  
                Q(leave_start__isnull=True)
            ).count()
        else:
            count = details.objects.filter(
                status=s, leave_start__lte=today
            ).count()

        leave_data.append({"kind": s, "count": count})
        total_strength += count

    template = get_template('activities/accounting.html')
    html = template.render({
        "logo_url": request.build_absolute_uri('../../static/media/images/cissg logo png.png'),
        "report_date": today.strftime("%d %B %Y"),
        "leave_data": leave_data,
        "total_strength": total_strength,
    })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{timestamp}_Accounting_Personnel.pdf"'
    pisa.CreatePDF(html, dest=response)

    return response


def add_leave(request):
     if request.method == 'POST':
          leave = request.POST.get('leave', '').strip()

          if not leave:
               messages.error(request, "Leave type cannot be empty.")
               return redirect('/admin_dashboard')

          # Check if this leave already exists
          if leaves.objects.filter(leave__iexact=leave).exists():
               messages.error(request, f"'{leave}' already exists.")
               return redirect('/admin_dashboard')

          # Save the new leave
          try:
               data = leaves(leave=leave)
               data.save()
               messages.success(request, f"'{leave}' Leave / Status has been added successfully.")
          except Exception as e:
               messages.error(request, f"Error adding leave: {str(e)}")

          return redirect('/admin_dashboard')

     # If GET request
     return render(request, 'add_leave.html')

def delete_leave(request, id):
     if request.method == 'POST':
          selected_ids = request.POST.getlist('selected_ids')
          if selected_ids:
               leaves.objects.filter(id__in=selected_ids).delete()
               messages.success(request, "Selected leave type(s) have been deleted.")
          else:
               messages.error(request, "No leave types were selected for deletion.")
          return redirect('/admin_dashboard')
     return redirect('/admin_dashboard')


def leave_record(request):
     leave = record.objects.all()
     today = date.today()
     context = {
          'leave': leave,
          'today': today,
     }
     return render(request, 'activities/leaves.html', context)


def edit_leave(request, id):
     if request.method == 'POST':
          
          leave = request.POST.get('leave')
          startdate = request.POST.get('startdate')
          enddate = request.POST.get('enddate')
          address = request.POST.get('address')
          order = request.POST.get('order')
          status = request.POST.get('status')
          record.objects.filter(id=id).update(
                                              leave = leave,
                                              startdate=startdate,
                                              enddate=enddate,
                                              address=address,
                                              order=order,
                                              status=status)

          return redirect('/leave_record')
     
     return redirect('/leave_record')