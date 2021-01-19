from django.db import models


# Create your models here.

class AbstractclassforProduct(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    upload = models.ImageField()


class Products(AbstractclassforProduct):
    product_id = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

class Categories(AbstractclassforProduct):
    category_id = models.CharField(max_length=100)
