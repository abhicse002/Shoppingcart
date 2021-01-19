from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_fname = models.CharField(max_length=100,default='foo')
    customer_lname = models.CharField(max_length=100,default='foo')
    customer_address =models.CharField(max_length=100,default='foo')
    customer_id = models.CharField(max_length=100,default='foo')
    customer_phone = models.CharField(max_length=12,default='foo')
    customer_email = models.CharField(max_length=100,default='foo')
