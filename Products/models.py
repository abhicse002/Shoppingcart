from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc =models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)

