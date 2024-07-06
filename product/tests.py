from rest_framework.test import APITestCase
from .models import Product


class Test_product_creat(APITestCase):
    def test_create_product(self):
        Product.objects.create(name='Product Name', content='zwerxdctfybu', price=100)

        data = {
            'name': 'Product Name',
            'content': 'zwerxdctfybu',
            'price': 100

        }

        response = self.client.post('/product/create/', data=data)
        self.assertEqual(response.status_code, 201)
