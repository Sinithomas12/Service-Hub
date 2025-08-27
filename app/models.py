from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.EmailField(max_length=100,null=True)
    password = models.CharField(max_length=100, null=True)
    userType = models.CharField(max_length=100, null=True) 
    def __str__(self):
        return self.email or"Login"
from django.db import models

# --- Choice Lists ---
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected')
]

# Better for availability tracking
JOB_STATUS_CHOICES = [
    ('available', 'Available'),      # Free to be booked
    ('busy', 'Busy'),                # Currently working
    ('completed', 'Completed')       # Job done, free again
]



# --- Login Model ---
class Login(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    userType = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.email
    
class Category(models.Model):
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return self.category



# --- Workers Registration ---

class WorkersReg(models.Model):
    worid = models.ForeignKey(
        Login,
        on_delete=models.CASCADE,
        null=True,
        related_name="workers"
    )
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='workers/', null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    wages = models.CharField(max_length=100, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    jobstatus = models.CharField(max_length=20, choices=JOB_STATUS_CHOICES, default="available")

    def __str__(self):
        return f"{self.name} ({self.category})"


# --- Users Registration ---
class UserReg(models.Model):
    usrid = models.ForeignKey(
        Login, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name="users"
    )
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return self.name

class Contactus(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)  # Better for long messages

    def __str__(self):
        return self.name or "No Name"
class Booking(models.Model):
    user=models.ForeignKey(UserReg,on_delete=models.CASCADE)
    worker=models.ForeignKey(WorkersReg,on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[("booked", "Booked"), ("completed", "Completed"), ("cancelled", "Cancelled")],
        default="booked"
    )
    def __str__(self):
        return f"{self.user.name} booked {self.worker.name}"