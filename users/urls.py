from django.urls import path, include
from . import views as users_views

urlpatterns = [
    path('', users_views.home, name='home'),
    path('contact_us/', users_views.contactUs, name='contact-us'),
    path('featured/', users_views.featuredCars, name='featured'),
    path('testdrive/', users_views.testDrive, name='test-drive'),
]
