import importlib
from unicodedata import name
from django.shortcuts import render ,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Vendor
from django.contrib import messages
from product.models import Product,Category
# Create your views here.
def become_vendor(request):
    if request.method == 'POST':
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            
            vendor = Vendor.objects.create(name=user.username, created_by=user)
            messages.success(request, f"welcome{user}")
            return redirect('core:frontpage')
        else:
            messages.error(request,"somthing wrong plz registed again")
            return redirect('become_vendor')
    form = UserCreationForm()        
    return render (request,'vendor/become_vendor.html',{'form':form})




@login_required
def vender_admin(request):
    
    vendor = request.user.ven
    products = vendor.products.all()

    
    return render(request,'vendor/vendor_admin.html',{
        'vendor':vendor,
        'products':products,
        })