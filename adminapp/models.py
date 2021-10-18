from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class banner(models.Model):
    bannername = models.CharField(max_length=40)
    bannerimage = models.CharField(max_length=60)


class brand(models.Model):
    brandname = models.CharField(max_length=40)
    brandimage = models.CharField(max_length=60)
