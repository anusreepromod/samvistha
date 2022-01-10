from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.EmailField()


class login(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=20)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)


class address(models.Model):
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.IntegerField()
    mobile = models.BigIntegerField()
    addresstype = models.CharField(max_length=30)
