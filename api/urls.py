from django.urls import path, include
from api import views as api_views

#Django API part3 tut
# from rest_framework.authtoken.views import obtain_auth_token #For giving the user the token


urlpatterns = [
    
    # Customers
    path('users/customers/', api_views.CustomersView.as_view(), name = 'customers'),
    # Managers
    path('users/managers/', api_views.ManagersView.as_view(), name = 'managers'),
    # Sale Associates
    path('users/associate/', api_views.AssociatesView.as_view(), name = 'associates'),
    # Rental Packages
    path('rental_package/', api_views.RentalPackagesView.as_view(), name = 'rentalPackages'),
    # Vehicles
    path('vehicles/info/', api_views.VehiclesView.as_view(), name = 'vehicles'),
    # Insurances
    path('vehicles/insurance/', api_views.InsurancesView.as_view(), name = 'insurances'),
    # Bookings
    path('booking/list/', api_views.BookingsView.as_view(), name = 'bookings'),
    
]