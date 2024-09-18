from django import forms
from .models import Product

class  ProductForm(forms.ModelForm):
    name = forms.CharField(required=True,label="product name",widget=forms.widgets.TextInput(attrs={"palce-holder":"product name",'class':'form-control mt-3'}))
    price = forms.IntegerField(required=True,label="product price",widget=forms.widgets.NumberInput(attrs={"palce-holder":"product price",'class':'form-control mt-3'}))
    brand = forms.CharField(required=True,label="product brand",widget=forms.widgets.TextInput(attrs={"palce-holder":"product brand",'class':'form-control mt-3'}))
    category = forms.CharField(required=True,label="product category",widget=forms.widgets.TextInput(attrs={"palce-holder":"product category",'class':'form-control mt-3'}))
    class Meta:
        model = Product
        fields = ['name','price','brand','category']
