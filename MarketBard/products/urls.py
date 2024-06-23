
from django.urls import path
from products.views import index, products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:page>/', products, name='page'),
    path('/category/<int:category_id>/', products, name='category'),
    path('/category/<int:category_id>/<int:page>/', products, name='category_page'),
]
