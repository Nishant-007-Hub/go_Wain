from django.db import models
from django.db.models.fields import DateTimeField


# Create your models here.
class Product(models.Model):
    objects = None
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    brand_name = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    identificaion = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=110)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.order_json


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc

 

