from django.shortcuts import render

# Create your views here.
#################################################
#from pip install djangorestframework
#Part1
from rest_framework.response import Response
from rest_framework.views import APIView
#part2
from .serializers import PostSerializer
from .models import Post
#part3 
from rest_framework.permissions import IsAuthenticated
#part4 Look at different API views
from rest_framework import generics
from rest_framework import mixins

class PostView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        #send an email
        serializer.save()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostCreateView(
    mixins.ListModelMixin,
    generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #doesn't do the get request if only code is up to here 

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


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