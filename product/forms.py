from django import forms

class  AddToCart(forms.Form):
    quantity = forms.IntegerField()