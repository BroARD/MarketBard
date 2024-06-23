from django.shortcuts import render
from products.models import Products, ProductCategory


# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(request):
    context = {
        'products': Products.objects.all(),
        'category': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)