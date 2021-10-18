from django.shortcuts import render
from . models import *
from adminapp.models import *
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
        return render(request, 'dashboards.html', {'username': log_obj})
    except Exception as e:
        print(e)

    return render(request, 'logins.html')


def dashboards(request):
    banners = banner.objects.all
    return render(request, 'dashboards.html', {'banner': banners})


def ethnic(request):
    return render(request, 'ethnicwear.html')


def western(request):
    return render(request, 'westernwear.html')


def description(request):
    return render(request, 'descriptionpage.html')


def cart(request):
    return render(request, 'cart.html')
