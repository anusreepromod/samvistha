from django.urls.conf import path


from . import views

urlpatterns = [
    path('login/', views.logins, name="logins"),
    path('brand/', views.fnbrand, name="brand"),
    path('loadbrand/', views.loadbrand, name='loadbrand'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('category/', views.fncategory, name="category"),
    path('subcategory/', views.fnsubcategory, name="subcategory"),
    path('subsubcategory/', views.subsubcategory, name="subsubcategory"),
    path('getcategory/', views.getcategory, name='getcategory'),
    path('getsubcategory/', views.getsubcategory, name='getsubcategory'),
    path('orderdetails/', views.orderdetails, name="orderdetails"),
    path('discount/', views.discounts, name="discount"),
    path('fndiscount/', views.fndiscount, name='fndiscount'),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('addproducts/', views.fnaddproduct, name="addproducts"),
    path('productpage/', views.productpage, name="productpage"),
    path('checkproduct/', views.checkproduct, name='checkproduct'),
    path('banner/', views.fnbanner, name="banner"),
    path('allorders/', views.allorders, name="allorders"),
    path('customer/', views.customer, name="customer"),
    # path('productimage/', views.fnproductimage, name="productimage"),
    path('stock/', views.fnstock, name='stock'),
    path('notification/', views.notifications, name='notification'),
    path('addnotifications/', views.addnotifications, name='addnotifications'),
    path('getdata/', views.getdata, name='getdata'),
    path('stockcategory/', views.stockcategory, name='stockcategory'),
    path('stocksubcategory/', views.stocksubcategory, name='stocksubcategory'),
    path('getproductid/', views.getproductid, name='getproductid'),
    path('logout/', views.logout, name='logout'),
    path('fnorder/', views.fnorder, name='fnorder'),
    path('fnproductpage/', views.fnproductpage, name='fnproductpage'),
    path('updateprice/', views.updateprice, name='updateprice'),
    path('getprice/', views.getprice, name='getprice'),
    path('delproduct/', views.delproduct, name='delproduct'),
    path('deldiscount/', views.deldiscount, name='deldiscount'),
    path('master/', views.master),
    # path('update/', views.update)

]
