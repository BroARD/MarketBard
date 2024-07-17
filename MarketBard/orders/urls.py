from django.urls import path
from django.contrib.auth.decorators import login_required
from orders.views import OrdersListView, CreateOrderView, OrderView

app_name = 'orders'

urlpatterns = [
    path('', OrdersListView.as_view(), name='index'),
    path('order-create/', CreateOrderView.as_view(), name='create'),
    path('order/<int:pk>/', OrderView.as_view(), name='order')
]