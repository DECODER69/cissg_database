from django.shortcuts import render

from .models import extenduser, academic, other_trainings,vocational, coastguard, coastguard_foreign, coastguard_local, military, military_local, military_foreign, appointments, shipboard, collateral, shorebased, collateral2, government, nongovernment, cgawards, cglcommendation, cgappreciation, cgplaque, mawards, mlcommendation, mappreciation, mplaque, clcommendation, cappreciation, cplaque, career, organization, eligibility, retirement
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
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
               data.save()
               return render(request, 'activities/index.html')
          
def login(request):
     details = extenduser.objects.all()
     context = {
          'details': details
     }
     return render(request, 'activities/login.html', context)

def dashboard(request):
     data = extenduser.objects.filter(serialnumber = request.user)
     user = request.user

     context = {
          'data': data,
          'user': user
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