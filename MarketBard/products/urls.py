
from django.urls import path
from products.views import basket_add, basket_del, ProductsListView

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('<int:page>/', ProductsListView.as_view(), name='page'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('category/<int:category_id>/<int:page>/', ProductsListView.as_view(), name='category_page'),
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket_del/<int:product_id>/', basket_del, name='basket_del'),
]
