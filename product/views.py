from django.shortcuts import render,get_object_or_404
import random
from .models import Category,Product
from django.db.models import Q  
# Create your views here.
def search(request):
    query = request.GET.get('query','')
    products = Product.objects.filter(Q(title__icontains=query)| Q(descripion__icontains=query))
    return render(request,'product/search.html',
                  {
                      'query':query,
                      'products':products
                  })
    

def productview(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    return render(request, 'product/product.html', {'product': product, 'similar_products': similar_products})
 
 
def category(request, category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    return render(request,'product/category.html',{'category':category}) 