from django.urls import path
from . import views
app_name = 'product'


urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/',views.productview,name='product'),
    path('<slug:category_slug>/',views.category,name='category')
]
