from django.shortcuts import render

from .models import extenduser, academic
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
     user = request.user
     context = {
          'data': data,
          'user': user,
          'acad':acad
     }
     print("data", data)
     return render(request, 'activities/education.html', context)
          

     
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
