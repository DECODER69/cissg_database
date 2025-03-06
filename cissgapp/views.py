from django.shortcuts import render

from .models import extenduser
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
                    print("gago")
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
          
