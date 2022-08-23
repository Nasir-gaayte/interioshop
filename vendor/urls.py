from sys import float_repr_style
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_naem = 'vendor'

urlpatterns = [
    path('become_vendor/',views.become_vendor,name='become_vendor'),
    path('vendor_admin/',views.vender_admin,name='vendor_admin'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='vendor/login.html'),name='login'),
]
