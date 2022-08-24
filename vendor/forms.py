from django import forms

from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','image','title','description','price']