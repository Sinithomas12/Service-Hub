"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from app import views
# from django.conf.urls.static import static
# import os
# from django.conf import settings

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index),
#     path('services/', views.services),
#     path('about/', views.about),
#     path('login/', views.login),
#     path('userregistration/', views.userregistration),
#     path('workerregistration/', views.workerregistration),
#     path('contactus/', views.contact),
#     path('adminhome/', views.adminhome,name="adminhome"),
#     path('addcategory/', views.addcategory),
#     path('viewuser/', views.viewuser),
#     path('viewworker/', views.viewworker),
#     path("viewcategory/", views.viewcategory),
#     #path('userhome/', views.userhome),
#     path('userhome/', views.userhome, name='userhome'), 
#     path("userviewcategory/", views.userviewcategory),
#     path("bookingcategory/", views.bookingcategory, name="bookingcategory"),
#     path('approveworker/', views.approveworker),
#     path('rejectedworker/', views.rejectedworker),
#     path("book-worker/<int:worker_id>/", views.book_worker, name="book_worker"),
#     path('workerhome/',views.workerhome,name="workerhome"),
#     path("workerviewbooking/", views.workerbooking, name="workerbooking"),
#     path("worker/complete-booking/<int:booking_id>/", views.completebooking, name="completebooking"),
#     path('book-worker/<int:worker_id>/', views.book_worker, name='book_worker'),

#     # Stripe Checkout (create session)
#     path('checkout-stripe/<int:booking_id>/', views.checkout_stripe, name='checkout_stripe'),

#     # Booking success page (after payment)
#     path('booking-success/<int:booking_id>/', views.booking_success, name='booking_success'),

    
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Public pages
    path('', views.index),
    path('services/', views.services),
    path('about/', views.about),
    path('contactus/', views.contact),

    # Authentication / Registration
    path('login/', views.login),
    path('userregistration/', views.userregistration),
    path('workerregistration/', views.workerregistration),

    # Admin dashboard
    path('adminhome/', views.adminhome, name='adminhome'),
    path('addcategory/', views.addcategory),
    path('viewuser/', views.viewuser),
    path('viewworker/', views.viewworker, name="viewworker"),
    path('viewcategory/', views.viewcategory, name='viewcategory'),
    path('viewpayment/',views.viewpayment),
    path("editworker/<int:id>/", views.editworker, name="editworker"),
    path('deleteworker/<int:id>/', views.deleteworker, name='deleteworker'),
    path('editcategory/<int:id>/', views.editcategory, name='editcategory'), # Edit a category
    path('deletecategory/<int:id>/', views.deletecategory, name='deletecategory'), # Delete a category
    # Admin booking URLs
    path('viewbooking/', views.viewbooking, name="viewbooking"),
    path('completebooking/<int:id>/', views.admin_complete_booking, name="admin_completebooking"),
    path('cancelbooking/<int:id>/', views.admin_cancel_booking, name="admin_cancelbooking"),
    path('deletebooking/<int:id>/', views.delete_booking, name="admin_deletebooking"),
    path('deletepayment/<int:id>/', views.deletepayment, name="deletepayment"),

    path('viewpayment/', views.viewpayment, name="viewpayment"),
    path('contactus/', views.contactus, name='contactus'),
    path('admincontactus/', views.admincontactus, name='admincontactus'),

    # User dashboard
    path('userhome/', views.userhome, name='userhome'),
    path('userviewcategory/', views.userviewcategory),
    path('bookingcategory/', views.bookingcategory, name='bookingcategory'),
    path('approveworker/', views.approveworker),
    path('rejectedworker/', views.rejectedworker),
    path('cancelbooking/<int:id>/', views.cancelbooking, name='cancelbooking'),
    path('userviewbooking/', views.userviewbooking, name='userviewbooking'),
    path('userviewpayment/', views.userviewpayment, name='userviewpayment'),
    path('userprofile/', views.userprofile, name='userprofile'),
    
    # Worker booking / management
    path('book-worker/<int:worker_id>/', views.book_worker, name='book_worker'),
    path('checkout-stripe/<int:booking_id>/', views.checkout_stripe, name='checkout_stripe'),
    path('booking-success/<int:booking_id>/', views.booking_success, name='booking_success'),

    # Worker dashboard
    path('workerhome/', views.workerhome, name='workerhome'),
    path('workerviewbooking/', views.workerbooking, name='workerbooking'),
    path('worker/complete-booking/<int:booking_id>/', views.completebooking, name='completebooking'),
    path('workerviewpayment/', views.workerviewpayment, name='workerviewpayment'),
    path('workerprofile/', views.workerprofile, name='workerprofile'),
]

# Serve static and media files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
