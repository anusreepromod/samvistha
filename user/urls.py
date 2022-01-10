from django.urls.conf import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('dashboards/', views.dashboards, name='dashboards'),
    path('ethnic/', views.ethnic, name='ethnic'),
    path('description/<int:id>', views.description, name='description'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.logins, name='login'),
    path('signup/', views.signup, name='signup'),
    path('western/<str:name>', views.western, name='western'),
    path('kurta/', views.kurta, name='kurta'),
    path('skirt/', views.skirt, name='skirt'),
    path('payment/', views.fnpayment, name='payment'),
    path('getdata/', views.getdata, name='getdata'),
    path('logout/', views.fnlogout, name='logout'),
    path('setting/', views.fnsetting, name='setting'),
    path('profile/', views.fnprofile, name='profile'),
    path('addbag/', views.addbag, name='addbag'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
    path('updatepayment/', views.updatepayment, name='updatepayment'),
    path('delete/', views.fndelete, name='delete'),
    path('summary/', views.summary, name='summary'),
    path('masters/', views.masters),

]
