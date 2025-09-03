from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import WorkersReg, Booking, UserReg
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import WorkersReg, Booking, UserReg

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import WorkersReg, UserReg, Booking

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import WorkersReg, UserReg, Booking

from datetime import date as d, datetime as dt
import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from .models import Booking, Payment
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY  # Add 
# Create your views here.
                          ############## HOME ########################
def index(request):
    return render(request,'index.html')
def services(request):
    return render(request, 'services.html')
def about(request):
    return render(request, 'about.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Login, UserReg, WorkersReg

def login(request):
    msg = request.GET.get('msg', '')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Check if credentials match in Login table
            data = Login.objects.get(email=email, password=password)

            # Save common session data
            request.session['email'] = data.email
            request.session['userType'] = data.userType

            # Save user id depending on type
            if data.userType == "admin":
                request.session['userid'] = data.id   # store login table id for admin
                return redirect('adminhome')

            elif data.userType == "worker":
                worker = WorkersReg.objects.get(worid=data.id)  # match worker by Login FK
                request.session['userid'] = worker.id
                return redirect('workerhome')

            elif data.userType == "user":
                user = UserReg.objects.get(usrid=data.id)  # match user by Login FK
                request.session['userid'] = user.id
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
from django.shortcuts import get_object_or_404, render
from .models import Category, WorkersReg

def bookingcategory(request):
    servicetype = request.GET.get("type")
    selectedcategory = get_object_or_404(Category, category=servicetype)

    workers = WorkersReg.objects.filter(
        category=selectedcategory,
        status="approved"
    )

    return render(request, "user/bookingcategory.html", {
        "selectedcategory": selectedcategory,
        "workers": workers
    })

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


# def book_worker(request, worker_id):
#     # Get the worker user selected
#     worker = get_object_or_404(WorkersReg, id=worker_id)
#      # Get the logged-in user from session
#     user_id = request.session.get("userid")
#     user = get_object_or_404(UserReg, id=user_id)

#     # # Save category to stay on same page
#     # category = worker.category.category
#     # If the user submitted the booking form
#     if request.method == "POST":
#         # Get data from the form
#         bookingdatetime=request.POST.get("bookingdatetime") # time of booking
#         additionalinfo=request.POST.get("additionalinfo")# optional note
#         amount=500 # fixed payment amount (can be dynamic)
#          # Create a booking record in database
#         booking = Booking.objects.create(
#             user=user,
#             worker=worker,
#             bookingdatetime=bookingdatetime,
#             additionalinfo=additionalinfo
#         )
#         # Redirect back to the same category page
#         #return redirect(f'/bookingcategory/?type={category}')
    
#          # Create a payment record linked to this booking
#         Payment.objects.create(
#             booking=booking,
#             amount=amount,
#             status="pending"   # initially pending (not paid yet)
#         )
#            # If GET request, just show booking form

#         return redirect("checkout_stripe",booking_id=booking.id)
#        # For now we simulate redirecting to payment
#        # (in real case this would go to Stripe Checkout)

#     return render(request, "user/book_worker_form.html", {"worker": worker})
# def bookingsuccess(request,booking_id):
#         # Find the booking by ID
#     booking=get_object_or_404(Booking,booking_id)
#       # Get the payment related to this booking
#       #payment = Payment.objects.get(booking=booking)
#     payment=booking.payment
    
#     # ✅ Simulated payment confirmation:
#     # We are not checking with Stripe, just marking it as "paid"
#     payment.status="paid"
#     payment.stripe_payment_intent=request.GET.get("payment_intent","test_intent")
#     payment.save()

#     # Mark worker as busy (not available for other bookings)
#     booking.worker.jobstatus = "busy"
#     booking.worker.save()

#     # Show success page with booking and payment details
#     return render(request, "user/booking_success.html", {
#         "booking": booking,
#         "payment": payment,
#         "message": f"{booking.worker.name} booked successfully and payment received ✅"
#     })
# from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking, Payment, WorkersReg, UserReg
from datetime import datetime

# ------------------------------
# 1. Book a Worker
# ------------------------------
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from .models import Booking, Payment, WorkersReg, UserReg

stripe.api_key = settings.STRIPE_SECRET_KEY


# ------------------------------
# 1. Book a Worker
# ------------------------------
def book_worker(request, worker_id):
    user_id = request.session.get("userid")
    if not user_id:
        messages.error(request, "Please login to book a worker.")
        return redirect("login")

    user = get_object_or_404(UserReg, id=user_id)
    worker = get_object_or_404(WorkersReg, id=worker_id)

    if request.method == "GET":
        return render(request, "user/bookworkerform.html", {"worker": worker})

    if request.method == "POST":
        bookingdatetime = request.POST.get("bookingdatetime")
        additionalinfo = request.POST.get("additionalinfo", "")
        amount = 500  # fixed amount

        if not bookingdatetime:
            messages.error(request, "Please select a booking date and time.")
            return redirect("book_worker", worker_id=worker.id)

        try:
            bookingdatetime = datetime.strptime(bookingdatetime, "%Y-%m-%dT%H:%M")
        except ValueError:
            messages.error(request, "Invalid booking date and time format.")
            return redirect("book_worker", worker_id=worker.id)

        # Create booking
        booking = Booking.objects.create(
            user=user,
            worker=worker,
            bookingdatetime=bookingdatetime,
            additionalinfo=additionalinfo
        )

        # Create payment
        Payment.objects.create(
            booking=booking,
            amount=amount,
            status="pending"
        )

        messages.success(request, f"Booking for {worker.name} created! Proceed to payment.")
        return redirect("checkout_stripe", booking_id=booking.id)


# ------------------------------
# 2. Stripe Checkout
# ------------------------------
def checkout_stripe(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    payment = booking.payment

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'product_data': {'name': f'Booking {booking.worker.name}'},
                'unit_amount': int(payment.amount * 100),  # amount in paise
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(
            f'/booking-success/{booking.id}/?session_id={{CHECKOUT_SESSION_ID}}'
        ),
        cancel_url=request.build_absolute_uri(
            f'/book-worker/{booking.worker.id}/'
        ),
    )

    return redirect(session.url, code=303)


# ------------------------------
# 3. Booking Success Page
# ------------------------------
def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    payment = booking.payment

    payment.status = "paid"
    payment.stripe_payment_intent = request.GET.get("session_id", "stripe_session")
    payment.save()

    booking.worker.jobstatus = "busy"
    booking.worker.save()

    return render(request, "user/bookingsuccess.html", {
        "booking": booking,
        "payment": payment,
        "message": f"Booking for {booking.worker.name} completed successfully, and payment received ✅"
    })


     ############################### WORKER #################################

def workerhome(request):
    return render(request,'worker/workerhome.html')
def workerbooking(request):
    worker_id = request.session.get("userid")
    worker = get_object_or_404(WorkersReg, id=worker_id)  # Adjust field name if needed
    bookings = Booking.objects.filter(worker=worker).order_by("-booking_date")
    return render(request, 'worker/viewbookings.html', {
        "worker": worker,
        "bookings": bookings
    })
def completebooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    worker = booking.worker
    # Only allow the worker assigned to mark as completed
    if request.session.get("userid") == worker.id:
        booking.status = "completed"
        worker.jobstatus = "available"
        booking.save()
        worker.save()
        messages.success(request, "Booking marked as completed ✅")
    else:
        messages.error(request, "You cannot update this booking ❌")

    return redirect("workerbooking")
