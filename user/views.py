from email import message
import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Patients

# from PLMS.models import Patients 
# Create your views here. render(request,'user/login_register.html',context)


# def loginPage(request):
#   if request.user.is_authenticated:
#     return redirect('home')
#   if request.method=='POST':
#     username=request.POST.get('email')
#     password=request.POST.get('password')

#     try:
#       user=User.objects.get(username=username)
#     except:
#       messages.error(request,'User does not exits ')
#     user = authenticate(request,username=username,password=password)

#     if user is not None:
#       login(request,user)
#       return redirect('home')
#     else:
#       messages.error(request,'Email or password does not exists ')
#   context={}
#   return render(request,'user/login_register.html')

def loginPage(request):
  if request.method=='POST':
    try:
      userdetails=Patients.objects.get(patient_email=request.POST.get('email'),patient_password=request.POST.get('password'))
      print(userdetails)
      request.session['email']=userdetails.patient_email
      return redirect('home')
    except Patients.DoesNotExist as e:
      messages.success(request,'Password invalid')
    
  return render(request,'user/login_register.html')
# @login_required(login_url='login')
def home(request):
  return render(request,'user/home.html')

def logoutUser(request):
  # logout(request)
  try:
    del request.session['email']
  except:
    return redirect('login')
  return redirect('login')

def register(request):
  if request.method=='POST':
    print(request.POST)
    Username=request.POST.get('name')
    Email=request.POST.get('email')
    Password=request.POST.get('password')
    dob=request.POST.get('dob')
    phone=request.POST.get('phone')
    gender=request.POST.get('gender')
    Patients(patient_name=Username,patient_email=Email,patient_password=Password,patient_dob=dob,patient_gender=gender,patient_phone_number=phone,patient_status=1).save()
    messages.success(request,'The User '+request.POST.get('name')+'Is saved sucessfullt')
    return render(request,'user/register.html')
  else:
    return render(request,'user/register.html')