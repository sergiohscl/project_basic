from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()


class BaseTestCase(TestCase):
    def setUp(self):
        self.email = "samu@example.com"
        self.name = "samu"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.name, email=self.email, password=self.password
        )

        self.client = APIClient(enforce_csrf_checks=True)
        self.client.force_authenticate(user=self.user)


class CustomUserApiViewTest(BaseTestCase):
    def test_list_custom_user(self):
        # Testando a listagem de usuarios (GET)
        url = reverse('users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_custom_user_UNAUTHORIZED(self):
        self.client.force_authenticate(user=None)
        url = reverse('users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
