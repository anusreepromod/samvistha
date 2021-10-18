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
