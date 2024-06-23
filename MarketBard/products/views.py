from django.shortcuts import render
from products.models import Products, ProductCategory

from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(request, category_id=None, page=1):
    products = Products.objects.filter(category_id=category_id) if category_id else Products.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page=per_page)
    products_paginator = paginator.page(page)

    context = {
        'products': products_paginator,
        'category': ProductCategory.objects.all(),
        'category_id': category_id,
    }
    return render(request, 'products/products.html', context)