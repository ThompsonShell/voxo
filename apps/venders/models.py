from apps.products.models import Product
from django.db import models


class Vendor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    re_password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)
    image = models.ImageField(upload_to='venders')
    store_name = models.CharField(max_length=255)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    option = models.CharField(max_length=255)
    # permision

    def __str__(self):
        return self.first_name