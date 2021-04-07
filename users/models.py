from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta


# Create your models here.

class Login(models.Model):
    email_id = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True)
    password =   models.CharField(
        max_length=255, blank=False, default="Login")
    
     def __str__(self):
        return self.name
        
class Customer(models.Model):
    name = models.CharField(
        max_length=255, blank=False, default="Customer")
    gender= models.CharField(
        max_length=255, blank=False, default="Customer")
    age = models.IntegerField(default=18)
    phone_number = models.CharField(
        max_length=255, blank=False, default="Customer")
    drivers_license =  models.IntegerField(default=0, unique = True)
    email_id =  models.ForeignKey(Login, on_delete=models.CASCADE)
    
    
class Manager(model.Model):
    name = models.CharField(
        max_length=255, blank=False, default="Customer")
    gender= models.CharField(
        max_length=255, blank=False, default="Customer")
    age = models.IntegerField(default=18)
    phone_number = models.CharField(
        max_length=255, blank=False, default="Customer")
    manager_ssn =  models.IntegerField(default=0, unique = True)
    email_id =  models.ForeignKey(Login, on_delete=models.CASCADE)
    
    
class Sales_Associate(model.Model):
    name = models.CharField(
        max_length=255, blank=False, default="Customer")
    gender= models.CharField(
        max_length=255, blank=False, default="Customer")
    age = models.IntegerField(default=18)
    phone_number = models.CharField(
        max_length=255, blank=False, default="Customer")
    Ssn =  models.IntegerField(default=0, unique = True)
    email_id =  models.ForeignKey(Login, on_delete=models.CASCADE)
    
    
class Rental_Package(model.Model):
    per_day_rent = models.IntegerField(default=0)
    per_month_rent = models.IntegerField(default=0)
    touring_package= models.IntegerField(default=0)

class Booking(model.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(
        default=(datetime.now()+timedelta(minutes=5)))
    package_id = models.ForeignKey(Rental_Package, on_delete=models.CASCADE)
    sales_id = models.ForeignKey(Sales_Associate, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
class Customer_Service(model.Model):
    rate = models.IntegerField(default = 5)
    feedback = models.CharField(max_length=255, blank=False)
    bot_chat = models.BooleanField()
    customer_question = models.CharField(max_length=255, blank=False)
    sales_id = models.ForeignKey(Sales_Associate, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
class Vehicle(model.Model):
    price = models.IntegerField()
    make = models.CharField(max_length=255, blank=False)
    model =  models.CharField(max_length=255, blank=False)
    seating_cap = models.IntegerField()
    transmission = models.ChoiceField("Automatic","Manual")
    availability = models.BooleanField()
    
    
class Insurance(model.Model):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    insurance_prov = models.CharField(max_length=255, blank=False)
    price = models.IntegerField()
    

class Manager_creates_pack(model.Model):
    manager_id = models.ForeignKey(Manager, on_delete = models.CASCADE)
    package_id = models.ForeignKey(Rental_Package, on_delete = models.CASCADE)
    
class Customer_testdrive(model.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.CharField(max_length=255, blank=False)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(
        default=(datetime.now()+timedelta(minutes=5)))
    
    
    
    
    
 
