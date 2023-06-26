from django.test import TestCase
from django.urls import reverse
from .models import Product
# Create your tests here.

# check type of is_available
class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(product_name='product1', slug='product1', description='description1', price=100, stock=10, is_available=True)
        Product.objects.create(product_name='product2', slug='product2', description='description2', price=200, stock=20, is_available=False)

    def test_product_is_available(self):
        product1 = Product.objects.get(product_name='product1')
        product2 = Product.objects.get(product_name='product2')
        self.assertIs(product1.is_available, True)
        self.assertIs(product2.is_available, False)
