
from django.urls import path
from products.views import index, products, basket_add, basket_del

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:page>/', products, name='page'),
    path('category/<int:category_id>/', products, name='category'),
    path('category/<int:category_id>/<int:page>/', products, name='category_page'),
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket_del/<int:product_id>/', basket_del, name='basket_del'),
]
