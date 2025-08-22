from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

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
    msg = request.GET.get('msg', '')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Check if credentials match in Login table
            data = Login.objects.get(email=email, password=password)

            # Save session
            request.session['email'] = data.email
            request.session['userType'] = data.userType

            # Redirect based on user type
            if data.userType == "admin":
                return redirect('adminhome')   # use named url instead of render
            elif data.userType == "worker":
                return redirect('worker_home')
            elif data.userType == "user":
                return redirect('userhome')

        except Login.DoesNotExist:
            msg = "Invalid username or password provided"

    return render(request, 'login.html', {'msg': msg})

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
    msg = request.GET.get('msg', '')
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
        category_id = request.POST.get("Category")  # get the id from form
        wages = request.POST.get("Wages")
        image = request.FILES.get("image")
        
        if not image:
            msg = "Please upload an image"
            return render(request, 'workerregisteration.html', {"msg": msg, "cat": cat})

        if WorkersReg.objects.filter(email=email).exists() or Login.objects.filter(email=email).exists():
            msg = "Email already registered"
        else:
            # Create login record
            login_record = Login.objects.create(email=email, password=password, userType='worker')
            
            # Fetch the Category instance
            category_instance = Category.objects.get(id=category_id)
            
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
                category=category_instance,  # ✅ pass the instance
                wages=wages,
                worid=login_record
            )
            
            msg = "Registration Successful"



    return render(request, 'workerregisteration.html', {"msg": msg, "cat": cat})

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
def viewworker(request):
    abc = WorkersReg.objects.all()
    return render(request, 'admin/viewworker.html', {"abc": abc})
def viewcategory(request):
    abc=Category.objects.all()
    return render(request,'admin/viewcategory.html',{"abc":abc})






     ############################### USER#################################

def userhome(request):
    msg = ""
    msg = request.GET.get('msg')
    return render(request, 'user/userhome.html', {})
def userviewcategory(request):
    abc=Category.objects.all()
    return render(request,'user/userviewcategory.html',{"abc":abc})
from django.shortcuts import render, get_object_or_404
from .models import Category, WorkersReg

def bookingcategory(request):
    # 1) Get category name from query parameter (?type=Plumber)
    servicetype = request.GET.get("type")

    # 2) Ensure category exists
    selectedcategory = get_object_or_404(Category, category=servicetype)

    # 3) Fetch all workers under this category who are approved
    workers = WorkersReg.objects.filter(
        category=selectedcategory,
        status="approved"
    )

    # 4) Pass category + workers list to template
    return render(
        request,
        "user/bookingcategory.html",
        {
            "selectedcategory": selectedcategory,
            "workers": workers
        }
    )
def approveworker(request):
    workerid=request.GET.get("id")
    if workerid:
        WorkersReg.objects.filter(id=workerid).update(status="approved")
    msg="Worker approved"
    return HttpResponseRedirect("/viewworker?msg=" + msg)
def rejectedworker(request):
    workerid=request.GET.get("id")
    if workerid:
        worker=WorkersReg.objects.filter(id=workerid).first()
        if worker and worker.worid:
            worker.worid.delete()
    msg="Worker rejected and deleted"
    return HttpResponseRedirect("/viewworker?msg="+msg)
    