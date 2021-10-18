from django.urls.conf import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('dashboards/', views.dashboards, name='dashboards'),
    path('ethnic/', views.ethnic, name='ethnic'),
    path('description/', views.description, name='description'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.logins, name='login'),
    path('signup/', views.signup, name='signup'),
    path('western/', views.western, name='western'),
]
