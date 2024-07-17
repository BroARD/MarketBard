from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from orders.models import Order
from products.models import Basket
from orders.forms import CreateOrderForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class OrdersListView(ListView):
    template_name = 'orders/orders.html'
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = super(OrdersListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrdersListView, self).get_context_data()
        context['orders'] = Order.objects.all()
        return context

class CreateOrderView(CreateView):
    template_name = 'orders/order-create.html'
    model = Order
    form_class = CreateOrderForm
    success_url = reverse_lazy('orders:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CreateOrderView, self).get_context_data()
        context['baskets'] = Basket.objects.all()
        return context

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        baskets = Basket.objects.filter(user=self.request.user)
        form.instance.result = sum([basket.sum() for basket in baskets])
        form.instance.basket_history = [basket.de_json() for basket in baskets]
        baskets.delete()
        return super(CreateOrderView, self).form_valid(form)



class OrderView(DetailView):
    template_name = 'orders/order.html'
    model = Order

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderView, self).get_context_data()
        return context


