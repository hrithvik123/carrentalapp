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
    path('contact_us/', users_views.contactUs, name='contact-us'),
    path('featured/', users_views.featuredCars, name='featured'),
    path('testdrive/', users_views.testDrive, name='test-drive'),
]
