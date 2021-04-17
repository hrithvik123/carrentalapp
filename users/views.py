from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,  # import classbased views
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Vehicle, Booking, Rental_Package, User, Customer_Service, Customer_testdrive
# Create your views here.


def home(request):
    return render(request, 'users/index.html')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'gender', 'age', 'contactNo']
    template_name = 'users/profile.html'

    def form_valid(self, form):
        messages.success(self.request, f'Profile updated successfully')
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('home')


# View for List of cars available to customer
class UserVehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'users/vehicle_all.html'
    context_object_name = 'vehicles'

    def get_queryset(self):
        return Vehicle.objects.filter(availability=True)


# View for all vehicles in database, for admin
class AdminVehicleListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Vehicle
    template_name = 'staff/vehicle_all.html'
    context_object_name = 'vehicles'

    # check if user is admin
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


# View for admin to update car's availability
class AdminVehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vehicle
    fields = ['availability']
    template_name = 'staff/vehicle_edit.html'

    # check if user is admin
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('admin-vehicle-all')


# view for admin to create vehicle
class VehicleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vehicle
    fields = ['make', 'model', 'engine_no', 'seating_cap',
              'transmission', 'package', 'availability']
    template_name = 'staff/vehicle_new.html'

    # check if form is valid
    def form_valid(self, form):
        form.instance.price = 10000
        messages.success(self.request, f'Car Added')
        return super().form_valid(form)

    # check if user is admin
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('vehicle-all')


# View for List of rental packages for admin
class RentalListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Rental_Package
    template_name = 'staff/rental_all.html'
    context_object_name = 'rentals'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

# View for admin to update the Rental packages


class RentalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Rental_Package
    fields = ['per_day_rent', 'per_month_rent', 'touring_package']
    template_name = 'staff/rental_edit.html'

    def form_valid(self, form):
        messages.success(self.request, f'Rental package updated successfully')
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('rental-all')


# View for admin to create new rental packages
class RentalCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Rental_Package
    fields = ['type', 'per_day_rent', 'per_month_rent', 'touring_package']
    template_name = 'staff/rental_new.html'

    def form_valid(self, form):
        messages.success(self.request, f'Rental Added')
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('rental-all')


# View for customer to make a booking
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['vehicle', 'start_time', 'end_time']
    template_name = 'users/booking_new.html'

    def form_valid(self, form):
        form.instance.customer_id = self.request.user.customer
        form.instance.sales_id = None
        messages.success(self.request, 'Booking made successfully')
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(BookingCreateView, self).get_form(*args, **kwargs)
        form.fields['vehicle'].queryset = Vehicle.objects.filter(
            availability=True)
        return form

    def get_success_url(self):
        return reverse('booking-all')


# View for User to see his/her bookings
class UserBookingListView(LoginRequiredMixin, ListView):
    model = Booking
    context_object_name = 'bookings'
    template_name = 'users/booking_all.html'

    def get_queryset(self):
        return Booking.objects.filter(customer_id=self.request.user.customer)
    # def test_func(self):
    #     if self.request.user.is_superuser:
    #         return True
    #     return False


# View for Admin to see all bookings
class AdminBookingListView(LoginRequiredMixin, ListView):
    model = Booking
    context_object_name = 'bookings'
    template_name = 'staff/booking_all.html'

    # def test_func(self):
    #     if self.request.user.is_superuser:
    #         return True
    #     return False


class ContactUsCreateView(LoginRequiredMixin, CreateView):
    model = Customer_Service
    fields = ['customer_question', 'rate', 'feedback']
    template_name = 'users/contactus.html'

    def form_valid(self, form):
        form.instance.customer_id = self.request.user.customer
        form.instance.sales_id = None
        messages.success(self.request, 'Message sent successfully')
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(ContactUsCreateView, self).get_form(*args, **kwargs)
        return form

    def get_success_url(self):
        return reverse('contact-us')


class TestDriveCreateView(LoginRequiredMixin, CreateView):
    model = Customer_testdrive
    fields = ['customer_id', 'vehicle_id', 'route', 'start_time', 'end_time']
    template_name = 'users/testdrive.html'

    def form_valid(self, form):
        form.instance.customer_id = self.request.user.customer
        form.instance.sales_id = None
        messages.success(self.request, 'Message sent successfully')
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(TestDriveCreateView, self).get_form(*args, **kwargs)
        return form

    def get_success_url(self):
        return reverse('testdrive-all')


class UserViewTicket(LoginRequiredMixin, ListView):
    model = Customer_Service
    context_object_name = 'viewtickets'
    template_name = 'users/customer_service_tickets.html'


class UserTestDrive(LoginRequiredMixin, ListView):
    model = Customer_testdrive
    context_object_name = 'viewtestdrive'
    template_name = 'users/test_drive_view.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Customer_testdrive.objects.all()
        else:
            return Customer_testdrive.objects.filter(customer_id=self.request.user.customer)


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    fields = ['start_time', 'end_time']
    template_name = 'users/booking_edit.html'

    def form_valid(self, form):
        form.instance.sales_id = None
        messages.success(self.request, f'Booking updated successfully')
        return super().form_valid(form)

    def test_func(self):
        booking = self.get_object()
        if self.request.user.customer == booking.customer_id:
            return True
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('booking-all')


class BookingCancelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = "staff/booking_delete.html"

    def test_func(self):
        booking = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        messages.success(self.request, f'Booking deleted successfully')
        return reverse('admin-booking-all')


def contactUs(request):
    return render(request, "users/contactus.html")


def testDrive(request):
    return render(request, "users/testdrive.html")
