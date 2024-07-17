from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from products.models import Products

# Create your tests here.

class IndexViewTestCase(TestCase):

    def test_index(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/index.html')

class ProductListTestCase(TestCase):

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        products = Products.objects.all()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(list(products[:3]), list(response.context_data['object_list']))