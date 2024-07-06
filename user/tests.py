from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from user.models import User


class Test_login_api(APITestCase):

    def test_only_admins_can_log_in(self):
        User.objects.create_user(email='test@mail.com', password='test1234567', is_staff=True)

        tokens_count = Token.objects.count()

        self.assertEqual(tokens_count, 0)

        data = {
            "email": "a@gmail.com",
            "password": "1"
        }
        response = self.client.post('user/users/login/', data=data)

        self.assertEqual(response.status_code, 200)

        self.assertIn("token", response.data)

        tokens_count = Token.objects.count()
        self.assertEqual(tokens_count, 1)

    def test_invalid_email_password(self):
        User.objects.create_user(email='test@mail.com', password='test1234567', is_staff=True)

        tokens_count = Token.objects.count()

        self.assertEqual(tokens_count, 0)

        data = {
            "email": "test@mail.com",
            "password": "test1234568"
        }
        response = self.client.post('user/users/login/', data=data)

        self.assertEqual(response.status_code, 401)

        self.assertNotIn("token", response.data)

        tokens_count = Token.objects.count()
        self.assertEqual(tokens_count, 0)
