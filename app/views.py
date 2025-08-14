from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

from datetime import date as d, datetime as dt

# Create your views here.
                          ############## HOME ########################
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
                return render(request, 'admin/adminhome.html')
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
def workerregistration(request):
    msg = request.GET.get('msg', '')  # Default empty string if msg not passed
    cat = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        gender = request.POST.get("Gender")
        experience = request.POST.get("Experience")
        location = request.POST.get("Location")
        category = request.POST.get("Category")
        wages = request.POST.get("Wages")
        
        # Handle image upload
        image = request.FILES.get("image")
        if not image:
            msg = "Please upload an image"
            return render(request, 'workerregisteration.html', {"msg": msg})

        # Check if email is already registered
        if WorkersReg.objects.filter(email=email).exists() or Login.objects.filter(email=email).exists():
            msg = "Email already registered"
        else:
            # Create login record
            login_record = Login.objects.create(email=email, password=password, userType='worker')
            
            # Create worker record
            reg = WorkersReg.objects.create(
                name=name,
                email=email,
                phone=phone,
                password=password,
                address=address,
                image=image,
                gender=gender,
                experience=experience,
                location=location,
                category=category,
                wages=wages,
                worid=login_record
            )
            
            msg = "Registration Successful"

    return render(request, 'workerregisteration.html', {"msg": msg,"cat": cat})
def contact(request):
    msg = ""

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contactus.objects.create(
            name=name, email=email, message=message
        )
        msg = "Your message has been sent successfully."

    return render(request, 'contact.html', {"msg": msg})
                      
                      ################# HOME ###################

                        ############# ADMIN HOME #############

def adminhome(request):
    msg=""
    msg=request.GET.get('msg')
    return render(request,'admin/adminhome.html',{})
def addcategory(request):
    msg = ""
    if request.method == "POST":
        category = request.POST.get("Category")
        image = request.FILES.get("image")
        if Category.objects.filter(category=category).exists():
            msg = "Already Added"
        else:
            Category.objects.create(category=category, image=image)
            msg = "Added Successfully"
    return render(request, 'admin/addcategory.html', {"msg": msg})

def viewuser(request):
    abc = UserReg.objects.all()
    return render(request, 'admin/viewuser.html', {"abc": abc})



        