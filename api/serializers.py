#Part 2
from rest_framework import serializers
from users import models

# Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = (
            'gender',
            'age',
            'contactNo',
            'drivers_license',
        )

#Manager
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manager
        fields = (
            'gender',
            'age',
            'contactNo',
            'manager_ssn',
        )

# Sales Associate
class AssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sales_Associate
        fields = (
            'gender',
            'age',
            'contactNo',
            'Ssn',
        )

# Rental Package
class RentalPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rental_Package
        fields = (
            'type',
            'per_day_rent',
            'per_month_rent',
            'touring_package',
        )
  
# Vehicle      
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = (
            'engine_no',
            'price',
            'model',
            'seating_cap',
            'transmission',
            'availability',
            'package',
        )
        
# Insurance
class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Insurance
        fields = (
            'vehicle_id',
            'insurance_prov',
            'price',
        )

# Booking
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = (
            'start_time',
            'end_time',
            'vehicle',
            'sales_id',
            'customer_id',
            'amount'
        )
        