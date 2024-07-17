from django.db import models
from users.models import User
from products.models import Basket


# Create your models here.

class OrderQuerySet(models.QuerySet):
    def order_number(self):
        return self.id


class Order(models.Model):

    objects = OrderQuerySet.as_manager()

    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3

    status_choice = (
        (CREATED, 'Создано'),
        (PAID, 'Оплачено'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлено')
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    basket_history = models.JSONField(default=dict)
    status = models.SmallIntegerField(default=CREATED, choices=status_choice)
    creation_date = models.DateTimeField(auto_now_add=True)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    result = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        return f'Пользователь:  {self.first_name} Номер товара: {self.last_name}'

