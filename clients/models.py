from django.db import models
from django.contrib.auth.models import Permission, User
from datetime import date
import datetime
from django.utils import timezone



class Driver(models.Model):
    id=models.CharField(primary_key=True, max_length=6)
    lat=models.CharField( max_length=6)
    lng=models.CharField( max_length=6)
    lastUpdate=models.DateField(auto_now_add=False , default=date.today)

class Request(models.Model):
    idRequest=models.CharField(primary_key=True, max_length=6)  
    driver=models.ForeignKey(Driver,on_delete=models.CASCADE)
    RequestDate=models.DateField(auto_now_add=False, default=date.today) 
    latPickUp=models.CharField( max_length=6)
    lngpickup=models.CharField( max_length=6)



