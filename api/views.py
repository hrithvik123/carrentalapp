from django.shortcuts import render #already present

# Create your views here.
################################################################################
#Part1.1
# from django.http import JsonResponse

# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 23
#     }
#     return JsonResponse(data)

#Implementation of #Part1.1 to project 
# from django.http import JsonResponse
#Using Booking model
 
# def BookingAPI(request):
#     data = {
#         'start time': ["2021-04-14", "9:00:00"],
#         'end time': ["2021-04-14", "12:25:39"],
#         'Vehicle': "Ford", 
#         'Sales id': 1231524,
#         'Customer id': 12345676,
#         'Amount': 230.
#     }
#     return JsonResponse(data)


#Part1.2
#used djangorestframework a third party package
# pip install djangorestframework
# from rest_framework.views import APIView #api view for get, post and etc requests
# from rest_framework.response import Response #like Json response

# class TestView(APIView):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'name': 'john',
#             'age': 23
#         }
#         return Response(data)

#Implementation of #Part1.2 to project
# from rest_framework.views import APIView #api view for get, post and etc requests
# from rest_framework.response import Response #like Json response

# class BookingsAPI(APIView):
#     def get(self, request, *args, **kwargs):
#         data = {
#         'start time': ["2021-04-14", "9:00:00"],
#         'end time': ["2021-04-14", "12:25:39"],
#         'Vehicle': "Ford", 
#         'Sales id': 1231524,
#         'Customer id': 12345676,
#         'Amount': 230
#     }
#         return Response(data)

#################################################################################################
# #Part2
# implemetation of serializers
# from rest_framework.views import APIView #api view for get, post and etc requests
# from rest_framework.response import Response #like Json response

# from . import serializers
# from users import models

# class TestView(APIView):
#     def get(self, request, *args, **kwargs):
#         qs = models.Post.objects.all()
#         #when getting all 
#         serializer = serializers.PostSerializer(qs, many = True)
#         #when getting one or specific one
#         # post = qs.first()
#         # serializer = PostSerializer(post)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = serializers.PostSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#Part2 implmentation on project
# class BookingsAPI(APIView):
#     def get(self, request, *args, **kwargs):
#         qs = models.Booking.objects.all()
#         #when getting all 
#         serializer = serializers.PostSerializerBookings(qs, many = True)
#         #when getting one or specific one
#         # post = qs.first()
#         # serializer = PostSerializer(post)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = serializers.PostSerializerBookings(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

###########################################################################################

# #part3 
# from rest_framework.permissions import IsAuthenticated

# from rest_framework.views import APIView #api view for get, post and etc requests
# from rest_framework.response import Response #like Json response
# # from knox.auth import TokenAuthentication

# from . import serializers
# from users import models

# class TestView(APIView):

#     # authentication_classes = (TokenAuthentication,)
#     #part3
#     # permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         qs = models.Post.objects.all()
#         #when getting all 
#         serializer = serializers.PostSerializer(qs, many = True)
#         #when getting one or specific one
#         # post = qs.first()
#         # serializer = PostSerializer(post)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = serializers.PostSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

##################################################################################################
# #part4 Look at different API views

from rest_framework import generics
from rest_framework import mixins

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView #api view for get, post and etc requests
from rest_framework.response import Response #like Json response

from . import serializers
from users import models

#part4.1
class PostView(
    mixins.ListModelMixin,      
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# part4.2
class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

#part4.3
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
   
#part5 API update and delete
class PostDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
   
        
class PostUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
    