from django.contrib import admin
from .models import Products
# Register your models here.

#without this Products table will not be reflected in Admin page
admin.site.register(Products)