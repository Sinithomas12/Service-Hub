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

JOB_STATUS_CHOICES = [
    ('not completed', 'Not Completed'),
    ('in progress', 'In Progress'),
    ('completed', 'Completed')
]

# --- Login Model ---
class Login(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


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
    image = models.ImageField(max_length=100,null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    category = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    wages = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    jobstatus = models.CharField(max_length=20, choices=JOB_STATUS_CHOICES, default="not completed")

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


