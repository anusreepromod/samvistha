from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from random import random
from . models import *
from user.models import *
# Create your views here.


def logins(request):
    return render(request, 'login.html')


def fnbrand(request):
    try:
        brandname = request.POST['brandname']
        print(brandname)
        brandimage = request.FILES['brandimage']
        print(brandimage)
        brandimage_name = str(random())+brandimage.name
        print(brandimage_name)
        brandimage_obj = FileSystemStorage()
        brandimage_obj.save(brandimage_name, brandimage)
        brand_obj = brand(brandname=brandname, brandimage=brandimage_name)
        brand_obj.save()
        print(brand_obj)
        return render(request, 'banner.html', {'msg': 'Banner inserted successfully'})
    except Exception as e:
        print(e)
    return render(request, 'brand.html')


def dashboard(request):
    customer = user.objects.all()
    return render(request, 'dashboard.html', {'customer': customer})


def category(request):
    return render(request, 'category.html')


def subcategory(request):
    return render(request, 'subcategory.html')


def subsubcategory(request):
    return render(request, 'subsubcategory.html')


def orderdetails(request):
    return render(request, 'orderdetails.html')


def discount(request):
    return render(request, 'discount.html')


def addproduct(request):
    return render(request, 'addproduct.html')


def productpage(request):
    return render(request, 'productpage.html')


def fnbanner(request):
    try:
        bname = request.POST['bname']
        print(bname)
        bimage = request.FILES['bimage']
        print(bimage)
        bimage_name = str(random())+bimage.name
        print(bimage_name)
        bimage_obj = FileSystemStorage()
        bimage_obj.save(bimage_name, bimage)
        banner_obj = banner(bannername=bname, bannerimage=bimage_name)
        banner_obj.save()
        print(banner_obj)
        return render(request, 'banner.html', {'msg': 'Banner inserted successfully'})
    except Exception as e:
        print(e)
    return render(request, 'banner.html')


def allorders(request):
    return render(request, 'allorders.html')


def customer(request):
    customer = user.objects.all()

    return render(request, 'customer.html', {'customer': customer})
