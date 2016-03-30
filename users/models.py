from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_UNKNOWN = 'U'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = [
        (GENDER_UNKNOWN, 'Unknow'),
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]
    
    owner        = models.OneToOneField(User, primary_key = True)
    birth_date   = models.DateField(blank=True, null = True) 
    phone_number = models.CharField(blank=True, max_length=20)
    gender       = models.CharField(max_length=1, choices = GENDER_CHOICES, default = GENDER_UNKNOWN)
    image        = models.ImageField(upload_to='photos', max_length=254, blank = True)