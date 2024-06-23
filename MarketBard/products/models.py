from django.db import models

from users.models import User

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=128)
    descriptions = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='products_images')
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'Пользователь { self.user.username }, Товар: { self.product.name }'