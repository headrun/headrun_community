from django.db import models
from django.contrib.auth.models import User,AbstractUser

from base.models import BaseModel
# Create your models here.

LOCATION_CHOICES = (
    ("BENGALURU", "BENGALURU"),
    ("HYDERABAD", "HYDERABAD"),
    )
DESIGNATION_CHOICES=(
    ('SE','SE'),
    ('ASE', 'ASE'),
    ('SE','SE'),
    )


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Profile(BaseModel):
    user_id= models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    date_of_birth=models.DateField()
    designation=models.CharField(max_length = 30, choices = DESIGNATION_CHOICES,default='SE')
    work_location=models.CharField(max_length=30,choices = LOCATION_CHOICES,default='HYDERABAD')
    status=models.BooleanField(default=False)

def _str_(self):
    return self.user_name.username
    