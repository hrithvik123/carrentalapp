#Part 2
from rest_framework import serializers
from users import models

# from users import models
# from users.models import Post

#VERY similiar to forms
# from django import forms

# class PostForm(forms.ModelForm):
#         class Meta:
#             model = Post
#             fields = {
#                 'title', 'description'
#             }

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = (
            'title', 
            'description'
        )

class PostSerializerBookings(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = (
            'start_time',
            'end_time',
            'vehicle',
            'sales_id',
            'customer_id',
            'amount'
        )
        