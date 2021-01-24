from django.test import TestCase
from django.contrib.auth import  get_user_model
# Create your tests here.
from ShoppingCart.Customers.models import Customers


class UserManagersTests(TestCase):
    def test_create_user(self):
        Customers = get_user_model()
        cust = Customers.objects.create
