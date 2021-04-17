from django.shortcuts import render #already present

from rest_framework import generics
# from rest_framework import mixins

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView #api view for get, post and etc requests
from rest_framework.response import Response #like Json response

from . import serializers
from users import models
    
# Our project models

# Customers
class CustomersView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.all()
    
# Managers
class ManagersView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.ManagerSerializer
    queryset = models.Manager.objects.all()
    
# Sales Associates    
class AssociatesView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.AssociateSerializer
    queryset = models.Sales_Associate.objects.all()

# Rental Packages    
class RentalPackagesView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.RentalPackageSerializer
    queryset = models.Rental_Package.objects.all()

# Vehicles    
class VehiclesView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.VehicleSerializer
    queryset = models.Vehicle.objects.all()

#Insurances
class InsurancesView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.InsuranceSerializer
    queryset = models.Insurance.objects.all()
    
# Bookings 
class BookingsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.BookingSerializer
    queryset = models.Booking.objects.all()
