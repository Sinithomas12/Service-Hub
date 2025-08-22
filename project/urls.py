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
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
import os
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('services/', views.services),
    path('about/', views.about),
    path('login/', views.login),
    path('userregistration/', views.userregistration),
    path('workerregistration/', views.workerregistration),
    path('contactus/', views.contact),
    path('adminhome/', views.adminhome,name="adminhome"),
    path('addcategory/', views.addcategory),
    path('viewuser/', views.viewuser),
    path('viewworker/', views.viewworker),
    path("viewcategory/", views.viewcategory),
    #path('userhome/', views.userhome),
    path('userhome/', views.userhome, name='userhome'), 
    path("userviewcategory/", views.userviewcategory),
    path("bookingcategory/", views.bookingcategory, name="bookingcategory"),
    path('approveworker/', views.approveworker),
    path('rejectedworker/', views.rejectedworker),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)