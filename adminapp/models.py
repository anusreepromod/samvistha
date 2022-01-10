from django.db import models
from django.db.models.fields import CharField
from user.models import *
import uuid
# Create your models here.


class adminlogin(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=20)


class banner(models.Model):
    bannername = models.CharField(max_length=40)
    bannerimage = models.CharField(max_length=60)


class brand(models.Model):
    brandname = models.CharField(max_length=40)
    brandimage = models.CharField(max_length=60)
    status = models.CharField(max_length=40)


class category(models.Model):
    category_name = models.CharField(max_length=40)
    brand_id = models.ForeignKey(brand, on_delete=models.CASCADE)
    status = models.CharField(max_length=40)


class subcategory(models.Model):
    subcategory_name = models.CharField(max_length=40)
    subcategoryimage = models.CharField(max_length=60)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    status = models.CharField(max_length=40)


class notification(models.Model):
    notify = models.CharField(max_length=500)


class discount(models.Model):
    discounttype = models.CharField(max_length=40)
    discount = models.CharField(max_length=40)
    status = models.CharField(max_length=40)


class product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    brand_id = models.ForeignKey(brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(subcategory, on_delete=models.CASCADE)
    color = models.CharField(max_length=40)
    small = models.BooleanField()
    medium = models.BooleanField()
    large = models.BooleanField()
    xlarge = models.BooleanField()
    unitprice = models.CharField(max_length=40)
    purchaseprice = models.CharField(max_length=40)
    tax = models.CharField(max_length=40)
    fit = models.CharField(max_length=40)
    fabric = models.CharField(max_length=40)
    sleeve = models.CharField(max_length=40)
    discount = models.ForeignKey(discount, on_delete=models.CASCADE)
    pimage1 = models.CharField(max_length=50)
    pimage2 = models.CharField(max_length=50)
    pimage3 = models.CharField(max_length=50)
    status = models.CharField(max_length=40)


class stock(models.Model):
    productid = models.ForeignKey(product, on_delete=models.CASCADE)
    stock = models.CharField(max_length=40)


class addtobag(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.BigIntegerField()
    size = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    customerid = models.ForeignKey(user, on_delete=models.CASCADE)
    productid = models.ForeignKey(product, on_delete=models.CASCADE)
    status = models.CharField(max_length=40)
    order_date = models.CharField(max_length=50)
    order_id = models.UUIDField(
        default=uuid.uuid4, unique=True, db_index=True, editable=False)


# class order(models.Model):
#     brand = models.ForeignKey(brand, on_delete=models.CASCADE)
#     name = models.ForeignKey(product, on_delete=models.CASCADE)
#     price = models.CharField(max_length=50)
#     size = models.CharField(max_length=50)
#     status = models.CharField(max_length=50)
#     order_date = models.DateField()
#     customerid = models.ForeignKey(user, on_delete=models.CASCADE)
#     address = models.TextField()
