from django.core import serializers
from .models import Customers


from rest_framework import  serializers

class CustomerSerializer(serializers.Serializer):
    customer_fname = serializers.CharField(max_length=100,default='foo')
    customer_lname = serializers.CharField(max_length=100,default='foo')
    customer_address =serializers.CharField(max_length=100,default='foo')
    customer_id = serializers.CharField(max_length=100,default='foo')
    customer_phone = serializers.CharField(max_length=12,default='foo')
    customer_email = serializers.CharField(max_length=100,default='foo')