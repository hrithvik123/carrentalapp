from django.shortcuts import render #already present

# Create your views here.
################################################################################
#Part1.1
from django.http import JsonResponse

def test_view(request):
    data = {
        'name': 'john',
        'age': 23
    }
    return JsonResponse(data)

#Implementation of #Part1.1 to project 
# from django.http import JsonResponse
#Using Booking model
 
def BookingAPI(request):
    data = {
        'start time': ["2021-04-14", "9:00:00"],
        'end time': ["2021-04-14", "12:25:39"],
        'Vehicle': "Ford", 
        'Sales id': 1231524,
        'Customer id': 12345676,
        'Amount': 230.
    }
    return JsonResponse(data)


#Part1.2
#used djangorestframework a third party package
# pip install djangorestframework
from rest_framework.views import APIView #api view for get, post and etc requests
from rest_framework.response import Response #like Json response

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'john',
            'age': 23
        }
        return Response(data)

#Implementation of #Part1.2 to project
# from rest_framework.views import APIView #api view for get, post and etc requests
# from rest_framework.response import Response #like Json response

class BookingsAPI(APIView):
    def get(self, request, *args, **kwargs):
        data = {
        'start time': ["2021-04-14", "9:00:00"],
        'end time': ["2021-04-14", "12:25:39"],
        'Vehicle': "Ford", 
        'Sales id': 1231524,
        'Customer id': 12345676,
        'Amount': 230.
    }
        return Response(data)

#################################################################################################
# #Part2
# from .serializers import PostSerializer
# from users.models import Post
# #part3 
# from rest_framework.permissions import IsAuthenticated
# #part4 Look at different API views
# from rest_framework import generics
# from rest_framework import mixins

# class PostView(
#     mixins.ListModelMixin, 
#     mixins.CreateModelMixin,
#     generics.GenericAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def perform_create(self, serializer):
#         #send an email
#         serializer.save()
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class PostCreateView(
#     mixins.ListModelMixin,
#     generics.CreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     #doesn't do the get request if only code is up to here 

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class PostListCreateView(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class TestView(APIView):

#     #part3 
#     permission_classes = (IsAuthenticated, ) #This checks the authentication to get the API endpoints 

#     #part1 and 2 
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many = True)
#         return Response(serializer.data)
    
#     #part2 
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

################################################