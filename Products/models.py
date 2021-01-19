from django.db import models


# Create your models here.

class AbstractclassforProduct(models.Model):
    name = models.CharField(max_length=100, default='foo')
    desc = models.CharField(max_length=100, default='foo')
    upload = models.ImageField(default='')


class Products(AbstractclassforProduct):
    product_id = models.CharField(max_length=100, default='foo')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Categories(AbstractclassforProduct):
    category_id = models.CharField(max_length=100, default='foo')
