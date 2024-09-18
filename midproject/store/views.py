from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import Product
# Create your views here.


def products_list(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products' : products})


from .forms import ProductForm
def create_product(request):
    if request.method == 'POST':
        data = request.POST.dict()
        form = ProductForm(data)
        if form.is_valid():
            form.save()
            return redirect("/products")
        else : 
            return render(request,'create.html',{'form' : form})
    form = ProductForm()
    return render(request,'create.html',{'form' : form})


def update_product(request,id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST.dict()
        form = ProductForm(data,instance=product)
        if form.is_valid():
                form.save()
                return redirect("/products")
        else:
            return render(request,'create.html',{'form' : form})
    form = ProductForm(instance=product)
    return render(request,'update.html',{'form' : form})


def delete_product(request,id):
    if request.method == "POST" : 
        Product.objects.get(id = id).delete()
        return redirect("/products")
    return render(request , "delete.html")