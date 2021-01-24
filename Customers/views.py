from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
from rest_framework import  serializers
from django.core import serializers

from .CustomerSerialize import CustomerSerializer
from .models import Customers
# Create your views here.

def addcustomer(request):
    return HttpResponse("Hello")
def removecustomer(request):
    return HttpResponse("Hello")
def editcustomer(request):
    return HttpResponse("Hello")

def viewcustomer(request):
    objs = Customers.objects.all()
    cust_seri = CustomerSerializer(objs)
    cust_seri.data

    return HttpResponse(cust_seri.data, content_type='application/json')


