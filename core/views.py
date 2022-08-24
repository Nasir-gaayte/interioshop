from django.shortcuts import render
from product.models import Product
# Create your views here.
def frontpage(request):
    newproduct = Product.objects.all()[0:8]
    return render(request,'core/frontpage.html',{
        'newproduct':newproduct,
        })



def contact(request):
    return render(request,'core/contact.html',{})