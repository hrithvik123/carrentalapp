from django.urls import path, include
from . import views as users_views
from allauth.account.views import LoginView, LogoutView, PasswordResetView, SignupView


urlpatterns = [
    path('', users_views.home, name='home'),
    path('register/', SignupView.as_view(template_name='users/register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='reset_password'),
    path('profile/<int:pk>/', users_views.UserUpdateView.as_view(), name='profile'),
    path('contact_us/', users_views.ContactUsCreateView.as_view(), name='contact-us'),
    path('featured/', users_views.UserVehicleListView.as_view(), name='vehicle-all'),
    path('staff/vehicle/new',
         users_views.VehicleCreateView.as_view(), name='vehicle-new'),
    path('staff/vehicle/all',
         users_views.AdminVehicleListView.as_view(), name='admin-vehicle-all'),
    path('staff/vehicle/<int:pk>/edit',
         users_views.AdminVehicleUpdateView.as_view(), name='admin-vehicle-edit'),
    path('staff/rental/all', users_views.RentalListView.as_view(), name='rental-all'),
    path('staff/rental/<int:pk>/edit',
         users_views.RentalUpdateView.as_view(), name='rental-edit'),
    path('staff/rental/new', users_views.RentalCreateView.as_view(), name='rental-new'),
    path('booking/new', users_views.BookingCreateView.as_view(), name='booking-new'),
    path('booking/all', users_views.UserBookingListView.as_view(),
         name='booking-all'),
    path('staff/booking/all', users_views.AdminBookingListView.as_view(),
         name='admin-booking-all'),
    path('booking/<int:pk>/edit', users_views.BookingUpdateView.as_view(),
         name='booking-edit'),
    path('booking/<int:pk>/delete', users_views.BookingCancelView.as_view(),
         name='booking-delete'),
<<<<<<< HEAD
    path('testdrive/', users_views.TestDriveCreateView.as_view(), name='test-drive'),
    path('contact_us/customer_service_tickets.html', users_views.UserViewTicket.as_view(),
         name='ticket-all'),  # view all tickets
    path('testdrive/test_drive_view.html', users_views.UserTestDrive.as_view(), name ='testdrive-all'),
=======
    path('testdrive/', users_views.testDrive, name='test-drive'),
    path('contact_us/customer_service_tickets.html', users_views.UserViewTicket.as_view(),
         name='ticket-all'),  # view all tickets
>>>>>>> 1fe1747b7586acc4be3ac61a7245976efce80752
]
