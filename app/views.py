from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

from datetime import date as d, datetime as dt

# Create your views here.
def index(request):
    return render(request,'index.html')
def services(request):
    return render(request, 'services.html')
def about(request):
    return render(request, 'about.html')
def login(request):
    msg=request.GET.get('msg','')
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            data=Login.objects.get(email=email,password=password)
            request.session['email']=email
            request.session['userType']=data.userType

            if data.userType=="admin":
                return render(request,'')
            elif data.userType=="worker":
                return redirect('')
            elif data.userType=="user":
                return redirect('')
        except Login.DoesNotExist:
            msg="Invalid username or password provided"
    return render(request,'login.html',{'msg':msg})
def userregistration(request):
    msg=""
    msg=request.GET.get('msg')
    if request.POST:
        name=request.POST.get("Name")
        email=request.POST.get("Email") 
        phone=request.POST.get("Number") 
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        gender = request.POST.get("Gender")
        if UserReg.objects.filter(email=email).exists() or Login.objects.filter(email=email).exists():
            msg="Email already registered"
        else:
            abc=Login.objects.create(email=email,password=password,userType='user')
            abc.save()
            reg=UserReg.objects.create(name=name,email=email,address=address,     phone=phone, password=password, usrid=abc, gender=gender)
            reg.save()
            msg="Registration Successful"
    return render(request,'userregisteration.html',{"msg":msg})