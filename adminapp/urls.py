from django.urls.conf import path


from . import views

urlpatterns = [
    path('login/', views.logins, name="logins"),
    path('brand/', views.fnbrand, name="brand"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('category/', views.category, name="category"),
    path('subcategory/', views.subcategory, name="subcategory"),
    path('subsubcategory/', views.subsubcategory, name="subsubcategory"),
    path('orderdetails/', views.orderdetails, name="orderdetails"),
    path('discount/', views.discount, name="discount"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('productpage/', views.productpage, name="productpage"),
    path('banner/', views.fnbanner, name="banner"),
    path('allorders/', views.allorders, name="allorders"),
    path('customer/', views.customer, name="customer")
]
