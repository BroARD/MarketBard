from django.shortcuts import render
from products.models import Products, ProductCategory


# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(request, category_id=None):

    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Products.objects.filter(category=category)
    else:
        products = Products.objects.all()
    context = {
        'products': products,
        'category': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)