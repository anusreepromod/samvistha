from django.http.response import JsonResponse
from django.shortcuts import render
from . models import *
from adminapp.models import *
from user.models import *
from django.db.models import Sum
import datetime
import razorpay
# Create your views here.


def signup(request):
    try:
        email = request.POST['email']
        print(email)
        u_obj = login.objects.filter(username=email).exists()
        if u_obj == False:
            name = request.POST['name']
            print(name)
            mobile = request.POST['mobile']
            print(mobile)
            password = request.POST['password']
            print(password)
            user_obj = user(name=name, mobile=mobile, email=email)
            print(user_obj)
            user_obj.save()
            login_obj = login(username=email, password=password,
                              user_id_id=user_obj.id)
            login_obj.save()
            return render(request, 'logins.html', {'message': 'User registered successfully'})
        else:
            return render(request, 'signup.html', {'msg': 'User already exist'})
    except Exception as e:
        print(e)
    return render(request, 'signup.html')


def logins(request):
    try:
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)
        logi_obj = login.objects.get(username=username, password=password)
        print(logi_obj)
        request.session['log'] = logi_obj.id
        log_obj = user.objects.get(id=logi_obj.user_id_id)
        username = log_obj.name
        banners = banner.objects.all()
        category_obj = subcategory.objects.all()
        list = []
        list1 = []
        for i in category_obj:
            if i.subcategory_name in list1:
                pass
            else:
                list1.append(i.subcategory_name)
                list.append({'name': i.subcategory_name,
                            'id': i.id, 'image': i.subcategoryimage})
        print(list)
        return render(request, 'dashboards.html', {'username': username, 'banner': banners, 'category': list})
    except Exception as e:
        print(e)
    return render(request, 'logins.html')


def fnlogout(request):
    del request.session['log']
    return render(request, 'logins.html')


def dashboards(request):
    banners = banner.objects.all()
    category_obj = subcategory.objects.all()
    list = []
    list1 = []
    for i in category_obj:
        if i.subcategory_name in list1:
            pass
        else:
            list1.append(i.subcategory_name)
            list.append({'name': i.subcategory_name,
                         'id': i.id, 'image': i.subcategoryimage})
    print(list)
    # print(category_obj)
    return render(request, 'dashboards.html', {'banner': banners, 'category': list})


def ethnic(request):
    return render(request, 'ethnicwear.html')


def western(request, name):

    pro = subcategory.objects.filter(subcategory_name=name)

    list = []
    prod = []
    products = []
    for i in pro:
        list.append(i.id)
    for i in list:
        products = product.objects.filter(subcategory_id_id=i
                                          ).select_related('brand_id', 'subcategory_id')
        for j in products:
            prod.append({'id': j.id, 'name': j.brand_id.brandname, 'subname': j.name,
                        'purchaseprice': j.purchaseprice, 'pimage1': j.pimage1})
            print(prod)
    return render(request, 'westernwear.html', {'product': prod})


def kurta(request):

    return render(request, 'kurtas.html')


def skirt(request):

    return render(request, 'skirt.html')


def description(request, id):
    print(id)
    products = product.objects.get(
        id=id)
    print(products)
    # prod = [{'brand': i.brand_id.brandname} for i in products]
    # print(prod)
    return render(request, 'descriptionpage.html', {'product': products})


def cart(request):
    try:
        cpass = request.session['log']
        print(cpass)
        bag = addtobag.objects.filter(
            customerid_id=cpass, status='added_to_bag')
        total = addtobag.objects.filter(
            customerid_id=cpass, status='added_to_bag').aggregate(TOTAL=Sum('price'))['TOTAL']
        print(total)
        add = address.objects.get(userid_id=cpass)
        print(add)
        return render(request, 'cart.html', {'bag': bag, 'sum': total, 'address': add})
    except Exception as e:
        print(e)

    return render(request, 'cart.html')


def fnpayment(request):
    return render(request, 'payment.html')


def getdata(request):
    id = request.POST['id']
    print(id)
    subcategory_obj = product.objects.filter(subcategory_id_id=id)
    print(subcategory_obj)
    # return render(request, 'kurtas.html', {'product': subcategory_obj})
    return JsonResponse({'msg': "get"})


def fnsetting(request):
    try:
        cpass = request.session['log']
        print(cpass)
        cpass_obj = login.objects.get(id=cpass)
        opassword = request.POST['opassword']
        print(opassword)
        npassword = request.POST['newpassword']
        if cpass_obj.password == opassword:
            cpass_obj.password = npassword
            cpass_obj.save()
            return render(request, 'setting.html', {'msg': 'password changed successfully'})
    except Exception as e:
        print(e)
    return render(request, 'setting.html')


def fnprofile(request):
    try:
        cpass = request.session['log']
        print(cpass)
        if request.method == 'POST':
            addresss = request.POST['address']
            print(addresss)
            city = request.POST['city']
            print(city)
            state = request.POST['state']
            print(state)
            country = request.POST['country']
            print(country)
            pincode = request.POST['pincode']
            print(pincode)
            mobile = request.POST['mobile']
            print(mobile)
            addresstype = request.POST['atype']
            print(addresstype)
            address_obj = address(userid_id=cpass, address=addresss, city=city, state=state,
                                  country=country, pincode=pincode, mobile=mobile, addresstype=addresstype)
            address_obj.save()

            return render(request, 'profile.html', {'msg': 'Added', })
    except Exception as e:
        print(e)
    add = address.objects.get(userid_id=cpass)
    print(add)
    return render(request, 'profile.html', {'address': add})


def addbag(request):
    try:
        cpass = request.session['log']
        print(cpass)
        if 'log' in request.session:
            if request.method == 'POST':
                id = request.POST['id']
                print(id)
                brands = request.POST['brand']
                print(brands)
                name = request.POST['name']
                print(name)
                size = request.POST['size']
                print(size)
                price = request.POST['price']
                print(price)
                image = request.POST['image']
                print(image)
                date = datetime.date.today()
                print(date)
                customerid = cpass
                status = 'added_to_bag'
                bag = addtobag(brand=brands, name=name,
                               size=size, price=price, order_date=date, image=image, customerid_id=customerid, status=status, productid_id=id)
                bag.save()
                return JsonResponse({'msg': 'Added to Bag'})
    except Exception as e:
        print(e)
    return render(request, 'cart.html')


def updatepayment(request):
    userid = request.session['log']
    print(userid)
    addtobag.objects.filter(customerid_id=userid,
                            status='added_to_bag').update(status='paid')
    return JsonResponse({'msg': 'success'})


def orderproduct(request):
    userid = request.session['log']
    print(userid)
    products_order = addtobag.objects.filter(customerid_id=userid,
                                             status='added_to_bag')
    order_amount = request.POST['totalprice']
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'
    addres = request.POST['address']
    note = {'Shipping Address': addres}
    type(order_amount)
    client = razorpay.Client(
        auth=('rzp_test_Wr1xwjcVt38vN4', 'oAKaMywWONAxmEheCue7uHwN'))
    payment = client.order.create(
        {"amount": order_amount, "currency": order_currency, "receipt": order_receipt, 'notes': note})
    return JsonResponse(payment)


# def orderid(request):
#     userid = request.session['log']
#     print(userid)
#     orderid = request.POST['orderid']
#     addtobag.objects.filter(customerid_id=userid,
#                             status='paid').update(order_id=orderid)
#     return JsonResponse({'msg': 'msg'})
def fndelete(request):
    delid = request.POST['id']
    print(delid)
    addtobag.objects.filter(id=delid).delete()
    return JsonResponse({'msg': "data deleted succcessfully"})


def summary(request):
    return render(request, 'summary.html')


def masters(request):
    logid = request.session.get('log')
    print(logid)
    logi = login.objects.get(id=logid)
    print(logi.username)
    return JsonResponse({'user': logi.username, })
