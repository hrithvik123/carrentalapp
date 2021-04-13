from django.urls import path, include
from api import views as api_views

#Django API part3 tut
# from rest_framework.authtoken.views import obtain_auth_token #For giving the user the token


urlpatterns = [
    #Part1.1 
    path('part1_1', api_views.test_view, name = 'part1_1'),
    path('part1_1/bookings', api_views.BookingAPI, name = 'part1_1_bookings'),

    #Part1.2
    path('part1_2', api_views.TestView.as_view(), name = 'part1_2'),
    path('part1_2/bookings', api_views.BookingsAPI.as_view(), name = 'part1_2_bookings'),

    # path('api-auth/', include('rest_framework.urls')),
    #django API part3 tut
    # path('api/token/', obtain_auth_token, name='obain_token'), #where we get the token
    #Third party knox authentication
    # path('api/auth/', include('knox.urls')),
    # path('create/', api_views.PostCreateView.as_view(), name = 'testCreate'),
    # path('create2/', api_views.PostListCreateView.as_view(), name = 'testCreate2'),
]