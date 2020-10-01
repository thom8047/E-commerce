from django.shortcuts import render
from .models import Product

def store(request):
    products    = Product.objects.all()
    context     = {'products_list': products}

    return render(request, 'store.html', context)

def cart(request):
    contex = {}
    return render(request, 'cart.html', contex)

def checkout(request):
    contex = {}
    return render(request, 'checkout.html', contex)