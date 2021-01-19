from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_fname = models.CharField(max_length=100)
    customer_lname = models.CharField(max_length=100)
    customer_address =models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=12)
    customer_email = models.CharField(max_length=100)
