from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from random import random
from . models import *
from user.models import *
# Create your views here.


def logins(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            print(username)
            password = request.POST['password']
            print(password)
            logi_obj = adminlogin.objects.get(
                username=username, password=password)
            # print(logi_obj.id)
            request.session['log'] = logi_obj.id
            customer = user.objects.all()
            return render(request, 'dashboard.html', {'customer': customer})
    except Exception as e:
        print(e)
    return render(request, 'login.html')


def logout(request):
    del request.session['log']
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
        status = 1
        brand_obj = brand(brandname=brandname,
                          brandimage=brandimage_name, status=status)
        brand_obj.save()

        print(brand_obj)
        return render(request, 'brand.html', {'msg': 'Brand inserted successfully'})
    except Exception as e:
        print(e)
    brand_obje = brand.objects.all()
    return render(request, 'brand.html', {'brand': brand_obje})


def loadbrand(request):
    brands = brand.objects.filter(status=1)
    brand_obj = [{'id': i.id, 'bname': i.brandname,
                  'bimage': i.brandimage} for i in brands]
    return JsonResponse({'brand': brand_obj})


def dashboard(request):
    customer = user.objects.all()
    return render(request, 'dashboard.html', {'customer': customer})


def fncategory(request):
    try:
        cname = request.POST['categoryname']
        print(cname)
        # cname_obj = category.objects.filter(category_name=cname).exists()
        # if cname_obj == False:
        bname = request.POST.getlist('brandname')
        print(bname)
        status = 1
        for i in bname:
            print(i)
            category_obj = category(
                category_name=cname, brand_id_id=i, status=status)
            category_obj.save()
        return render(request, 'category.html', {'msg': 'category added successfully'})
        # else:
        #     return render(request, 'category.html', {'message': 'category already exist'})
    except Exception as e:
        print(e)
    cate_obj = category.objects.filter(status=1)
    brand_obj = brand.objects.filter(status=1)
    return render(request, 'category.html', {'category': cate_obj, 'brand': brand_obj})

# def fncategory(request):
#     try:
#         cname = request.POST['categoryname']
#         print(cname)
#         bname = request.POST['brandname']
#         print(bname)
#         cname_obj = category.objects.filter(
#             category_name=cname, brand_id_id=bname).exists()
#         if cname_obj == False:
#             category_obj = category(category_name=cname, brand_id_id=bname)
#             category_obj.save()
#             return render(request, 'category.html', {'msg': 'category added successfully'})
#         # else:
#         #     return render(request, 'category.html', {'message': 'category already exist'})
#     except Exception as e:
#         print(e)
#     cate_obj = category.objects.all()
#     brand_obj = brand.objects.all
#     return render(request, 'category.html', {'category': cate_obj, 'brand': brand_obj})


def fnsubcategory(request):
    try:
        subname = request.POST['subcategory']
        # subname_obj = subcategory.objects.filter(
        #     subcategory_name=subname).exists()
        # if subname_obj == False:
        categoryname = request.POST['category']
        subcategoryimage = request.FILES['subcategoryimage']
        print(subcategoryimage)
        subcategoryimage_name = str(random())+subcategoryimage.name
        print(subcategoryimage_name)
        subcategoryimage_obj = FileSystemStorage()
        subcategoryimage_obj.save(subcategoryimage_name, subcategoryimage)
        status = 1
        subcategory_obj = subcategory(
            subcategory_name=subname, subcategoryimage=subcategoryimage_name, category_id_id=categoryname, status=status)
        subcategory_obj.save()
        return render(request, 'subcategory.html', {'msg': 'Sub category added successfully'})
        # else:
        #     return render(request, 'subcategory.html', {'msgs': 'subcategory already exist'})
    except Exception as e:
        print(e)
    subcat_obje = subcategory.objects.filter(status=1)
    category_obj = category.objects.filter(status=1)
    return render(request, 'subcategory.html', {'subcategory': subcat_obje, 'category': category_obj})


def subsubcategory(request):
    return render(request, 'subsubcategory.html')


def orderdetails(request):
    return render(request, 'orderdetails.html')


def discounts(request):
    try:
        if request.method == 'POST':
            dtype = request.POST['dtype']
            print(dtype)
            discounts = request.POST['discount']
            print(discounts)
            status = 1
            discount_obj = discount(
                discounttype=dtype, discount=discounts, status=status)
            discount_obj.save()
            return render(request, 'discount.html', {'msg': "Discount added successfully"})
    except Exception as e:
        print(e)
    return render(request, 'discount.html')


def fndiscount(request):
    discounts = discount.objects.filter(status=1)
    discount_obj = [{'id': i.id, 'type': i.discounttype,
                     'discount': i.discount} for i in discounts]
    return JsonResponse({'discount': discount_obj})


def addproduct(request):

    brands = brand.objects.filter(status=1)
    disc = discount.objects.filter(status=1)
    return render(request, 'addproduct.html', {'discount': disc, 'brand': brands})


def fnaddproduct(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('pname')
            print(name)
            desc = request.POST.get('desc')
            print(desc)
            brand = request.POST.get('brand')
            print(brand)
            category = request.POST.get('category')
            print(category)
            subcategory = request.POST.get('subcategory')
            print(subcategory)
            color = request.POST.get('color')
            print(color)
            small = request.POST.get('small')
            print(small)
            medium = request.POST.get('medium')
            print(medium)
            large = request.POST.get('large')
            print(large)
            xlarge = request.POST.get('xlarge')
            print(xlarge)
            unitprice = request.POST.get('unitprice')
            print(unitprice)
            purchaseprice = request.POST.get('purchaseprice')
            print(purchaseprice)
            tax = request.POST.get('tax')
            print(tax)
            fit = request.POST.get('fit')
            print(fit)
            fabric = request.POST.get('fabric')
            print(fabric)
            sleeve = request.POST.get('sleeve')
            print(sleeve)
            discount = request.POST.get('discount')
            print(discount)
            pimage1 = request.FILES.get('pimage1')
            print(pimage1)
            pimage1_name = str(random())+pimage1.name
            print(pimage1_name)
            pimage1_obj = FileSystemStorage()
            pimage1_obj.save(pimage1_name, pimage1)
            pimage2 = request.FILES.get('pimage2')
            print(pimage2)
            pimage2_name = str(random())+pimage2.name
            print(pimage2_name)
            pimage2_obj = FileSystemStorage()
            pimage2_obj.save(pimage2_name, pimage2)
            pimage3 = request.FILES.get('pimage3')
            print(pimage3)
            pimage3_name = str(random())+pimage3.name
            print(pimage3_name)
            pimage3_obj = FileSystemStorage()
            pimage3_obj.save(pimage3_name, pimage3)
            status = 1
            product_obj = product(name=name, desc=desc, brand_id_id=brand, category_id_id=category, subcategory_id_id=subcategory, color=color, small=small,
                                  medium=medium, large=large, xlarge=xlarge, unitprice=unitprice, purchaseprice=purchaseprice, tax=tax, discount_id=discount, pimage1=pimage1_name, pimage2=pimage2_name, pimage3=pimage3_name, fit=fit, fabric=fabric, sleeve=sleeve, status=status)
            product_obj.save()
            return JsonResponse({'msg': "Product added successfully"})
    except Exception as e:
        print(e)
    return render(request, 'productpage.html')


def checkproduct(request):
    name = request.POST['pname']
    print(name)
    product_obj = product.objects.filter(name=name).exists()
    if product_obj == True:
        return JsonResponse({'msg': 'Product already exist'})


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


# def fnproductimage(request):
    try:
        if request.method == 'POST':
            productid = request.POST['pid']
            print(productid)
            pimage1 = request.FILES['pimage1']
            print(pimage1)
            pimage1_name = str(random())+pimage1.name
            print(pimage1_name)
            pimage1_obj = FileSystemStorage()
            pimage1_obj.save(pimage1_name, pimage1)
            pimage2 = request.FILES['pimage2']
            print(pimage2)
            pimage2_name = str(random())+pimage2.name
            print(pimage2_name)
            pimage2_obj = FileSystemStorage()
            pimage2_obj.save(pimage2_name, pimage2)
            pimage3 = request.FILES['pimage3']
            print(pimage3)
            pimage3_name = str(random())+pimage3.name
            print(pimage3_name)
            pimage3_obj = FileSystemStorage()
            pimage3_obj.save(pimage3_name, pimage3)
            productimage_obj = productimage(
                productid_id=productid, pimage1=pimage1_name, pimage2=pimage2_name, pimage3=pimage3_name)
            productimage_obj.save()
            return render(request, 'productimages.html', {'msg': 'Images added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'productimages.html')


def fnstock(request):
    try:
        if request.method == 'POST':
            productid = request.POST['pid']
            print(productid)
            stocks = request.POST['stock']
            print(stocks)
            stock_obj = stock(productid_id=productid, stock=stocks)
            stock_obj.save()

            return render(request, 'stocks.html', {'msg': 'Stocks added successfully'})
    except Exception as e:
        print(e)
    brands = brand.objects.all()
    return render(request, 'stocks.html', {'brand': brands})


def notifications(request):
    notify = notification.objects.all()
    return render(request, 'notification.html', {'notify': notify})


def addnotifications(request):
    try:
        if request.method == 'POST':
            notifi = request.POST['notify']
            print(notifi)
            notify_obj = notification(notify=notifi)
            notify_obj.save()
            return render(request, 'addnotification.html', {'msg': 'Notification created successfully'})
    except Exception as e:
        print(e)
    return render(request, 'addnotification.html')


def getcategory(request):
    try:
        if request.method == 'POST':
            brands = request.POST['brand']
            print(brands)
            category_obj = category.objects.filter(brand_id_id=brands)
            for i in category_obj:
                print(i.category_name)
                print(i.brand_id_id)
            cat_obj = [{'category_name': i.category_name, 'id': i.id}
                       for i in category_obj]
            print(cat_obj)
            return JsonResponse({'category': cat_obj})
    except Exception as e:
        print(e)


def getsubcategory(request):
    try:
        if request.method == 'POST':
            categories = request.POST['category']
            print(categories)
            category_obj = subcategory.objects.filter(
                category_id_id=categories)
            cat_obj = [{'subcategory_name': i.subcategory_name, 'id': i.id}
                       for i in category_obj]
            print(cat_obj)
            return JsonResponse({'subcategory': cat_obj})
    except Exception as e:
        print(e)


def stockcategory(request):
    try:
        if request.method == 'POST':
            brands = request.POST['brand']

            category_obj = category.objects.filter(brand_id_id=brands)
            cat_obj = [{'category_name': i.category_name, 'id': i.id}
                       for i in category_obj]
            print(cat_obj)
            return JsonResponse({'category': cat_obj})
    except Exception as e:
        print(e)


def stocksubcategory(request):
    try:
        if request.method == 'POST':
            categories = request.POST['category']

            category_obj = subcategory.objects.filter(
                category_id_id=categories)
            cat_obj = [{'subcategory_name': i.subcategory_name, 'id': i.id}
                       for i in category_obj]
            print(cat_obj)
            return JsonResponse({'subcategory': cat_obj})
    except Exception as e:
        print(e)


def getproductid(request):
    try:
        if request.method == 'POST':
            subcategories = request.POST['subcategory']
            print(subcategories)
            subcategory_obj = product.objects.filter(
                subcategory_id_id=subcategories)
            print(subcategory_obj)
            cat_obj = [{'id': i.id}
                       for i in subcategory_obj]
            print(cat_obj)
            return JsonResponse({'product': cat_obj})
    except Exception as e:
        print(e)


def getdata(request):
    categori = category.objects.filter(status=1)
    totalproduct = product.objects.filter(status=1)
    order = addtobag.objects.filter(status='paid')
    customer = user.objects.all()
    category_obj = [{'id': i.id} for i in categori]
    tp_obj = [{'id': i.id} for i in totalproduct]
    customer_obj = [{'id': i.id} for i in customer]
    order_obj = [{'id': i.id} for i in order]
    return JsonResponse({'tc': category_obj, 'tp': tp_obj, 'user': customer_obj, 'order': order_obj})


def fnorder(request):
    order = addtobag.objects.filter(status='paid').select_related('customerid')
    order_obj = [{'id': i.id, 'cname': i.customerid.name, 'pname': i.name, 'brand': i.brand,
                  'orderno': i.order_id, 'odate': i.order_date, 'amount': i.price, 'status': i.status} for i in order]
    return JsonResponse({'order': order_obj})


def fnproductpage(request):
    products = product.objects.filter(
        status=1).select_related('brand_id', 'subcategory_id')
    product_obj = [{'id': i.id, 'name': i.name, 'brand': i.brand_id.brandname,
                    'subcat': i.subcategory_id.subcategory_name, 'price': i.purchaseprice} for i in products]
    return JsonResponse({'product': product_obj})


def getprice(request):
    try:
        if request.method == 'POST':
            mid = request.POST['uid']
            price = product.objects.get(id=mid)
            price_obj = [{'id': price.id, 'price': price.purchaseprice,
                          }]
            return JsonResponse({'price': price_obj})
    except Exception as e:
        print(e)


def updateprice(request):
    try:
        if request.method == 'POST':
            id = request.POST['id']
            price = request.POST['price']

            product.objects.filter(id=id).update(
                purchaseprice=price)
            return JsonResponse({'msg': "Data updated successfully"})
    except Exception as e:
        print(e)


def delproduct(request):
    delid = request.POST['id']
    print(delid)
    product.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


def deldiscount(request):
    delid = request.POST['id']
    print(delid)
    discount.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


def master(request):
    logid = request.session.get('log')
    print(logid)
    logi = adminlogin.objects.get(id=logid)
    print(logi.username)
    return JsonResponse({'user': logi.username, })


def delproduct(request):
    delid = request.POST['id']
    print(delid)
    brand.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


# def update(request):
#     brand.objects.all().update(status=1)
#     category.objects.all().update(status=1)
#     subcategory.objects.all().update(status=1)
#     discount.objects.all().update(status=1)
#     return JsonResponse({'msg': 'msg'})
