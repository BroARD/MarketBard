from django.shortcuts import render, HttpResponseRedirect
from products.models import Products, ProductCategory

from django.core.paginator import Paginator
from products.models import Basket

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

def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_del(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    basket = baskets.first()
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

