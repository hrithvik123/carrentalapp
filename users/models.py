from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.


class User(AbstractUser):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True)
    age = models.IntegerField(max_length=2, default='21', blank=True)
    contactNo = models.PositiveIntegerField(
        max_length=10, default='0', blank=True)

    def __str__(self):
        return self.username


class Login(models.Model):
    email_id = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True)
    password = models.CharField(
        max_length=255, blank=False, default="Login")

    # def __str__(self):
    #     return self.name


class Customer(User):
    drivers_license = models.IntegerField(default=0)

    class Meta:
        # db_table = 'customer'
        # Add verbose name
        verbose_name = 'Customer'


class Sales_Associate(User):
    Ssn = models.IntegerField(default=0)

    class Meta:
        # db_table = 'sales_associate'
        # Add verbose name
        verbose_name = 'Sales Associate'


class Manager(User):
    manager_ssn = models.IntegerField(default=0)

    class Meta:
        # db_table = 'manager'
        # Add verbose name
        verbose_name = 'Manager'


class Rental_Package(models.Model):
    car_types = (
        ('Hatchback', 'Hatchback'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV')
    )
    type = models.CharField(max_length=15, unique=True, choices=car_types)
    per_day_rent = models.IntegerField(default=0)
    per_month_rent = models.IntegerField(default=0)
    touring_package = models.IntegerField(default=0)

    def __str__(self):
        return self.type


class Customer_Service(models.Model):
    rate = models.IntegerField(default=5)
    feedback = models.CharField(max_length=255, blank=False)
    customer_question = models.CharField(max_length=255, blank=False)
    sales_id = models.ForeignKey(
        Sales_Associate, on_delete=models.SET_NULL, null=True, default=None)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_question


class Vehicle(models.Model):
    transmission_choices = (
        ('A', 'Automatic'),
        ('M', 'Manual')
    )
    engine_no = models.CharField(max_length=20, blank=False, default=None)
    price = models.IntegerField()
    make = models.CharField(max_length=255, blank=False)
    model = models.CharField(max_length=255, blank=False)
    seating_cap = models.IntegerField()
    transmission = models.CharField(max_length=1, choices=transmission_choices)
    availability = models.BooleanField()
    package = models.ForeignKey(Rental_Package, on_delete=models.CASCADE)

    def __str__(self):
        return self.make+" "+self.model


class Booking(models.Model):
    # default start of booking is next day
    start_time = models.DateTimeField(
        default=(datetime.now()+timedelta(days=1)))
    end_time = models.DateTimeField(
        default=(datetime.now()+timedelta(hours=48)))  # default end time is 24hrs from booking.
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    sales_id = models.ForeignKey(
        Sales_Associate, on_delete=models.CASCADE, default=None, null=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)


class Insurance(models.Model):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    insurance_prov = models.CharField(max_length=255, blank=False)
    price = models.IntegerField()


# maybe we don't need this, we should manager creates rental package as M:N
# but it should actually be 1:N
class Manager_creates_pack(models.Model):
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE)
    package_id = models.ForeignKey(Rental_Package, on_delete=models.CASCADE)


class Customer_testdrive(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.CharField(max_length=255, blank=False)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(
        default=(datetime.now()+timedelta(minutes=5)))


# #Django API

# Part2
# from django.contrib.auth import get_user_model

# User = get_user_model() # already defined in our project
