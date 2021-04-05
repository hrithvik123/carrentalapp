from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'users/homepage.html')


def featuredCars(request):
    return render(request, 'users/featured_cars.html')


def contactUs(request):
    return render(request, "users/contactus.html")


def testDrive(request):
    return render(request, "users/testdrive.html")
