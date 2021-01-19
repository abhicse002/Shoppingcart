from django.db import models


# Create your models here.
class Sellers(models.Model):
    seller_name = models.CharField(max_length=100, default='')
