from django.urls import path, include
from api import views as api_views

#Django API part3 tut
# from rest_framework.authtoken.views import obtain_auth_token #For giving the user the token


urlpatterns = [
    #Part1.1 
    # path('part1_1/', api_views.test_view, name = 'part1_1'),
    # path('part1_1/bookings', api_views.BookingAPI, name = 'part1_1_bookings'),

    #Part1.2
    # path('part1_2/', api_views.TestView.as_view(), name = 'part1_2'),
    # path('part1_2/bookings', api_views.BookingsAPI.as_view(), name = 'part1_2_bookings'),

    #Part2
    # path('part2/', api_views.TestView.as_view(), name = 'part2'),
    # path('part2/bookings', api_views.BookingsAPI.as_view(), name = 'part2_bookings'),

    #Part3
    # path('part3/', api_views.TestView.as_view(), name = 'part3'),

    #Part4.1 
    path('part4.1/', api_views.PostView.as_view(), name = 'part4.1'),

    #Part4.2
    path('part4.2/', api_views.PostCreateView.as_view(), name = 'part4.2'),

    #Part4.3
    path('part4.3/', api_views.PostListCreateView.as_view(), name = 'part4.3'),
    
    #Part4.4
    path('post/edit/', api_views.PostUpdateView.as_view(), name = 'update'),
    path('post/delete/', api_views.PostDeleteView.as_view(), name = 'delete')

]