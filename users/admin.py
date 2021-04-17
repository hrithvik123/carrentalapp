from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (
    User, Customer, Sales_Associate, Manager,
    Rental_Package, Vehicle, Booking, Insurance, Customer_Service
)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Customer)
admin.site.register(Sales_Associate)
admin.site.register(Manager)
admin.site.register(Rental_Package)
admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Insurance)
admin.site.register(Customer_Service)
