from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.messages import get_messages

User = get_user_model()


class AuthViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword"
        )
        self.avatar = SimpleUploadedFile("avatar.jpg", b"file_content")

    def test_login_view_authenticated_user(self):
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)  # Deve retornar 200 (OK)

    def test_cadastro_view_authenticated_user(self):
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        response = self.client.get(reverse("cadastro"))
        self.assertEqual(response.status_code, 200)

    def test_valida_cadastro_view_success(self):
        data = {
            "nome": self.user.username,
            "email": self.user.email,
            "senha": self.user.password,
            "avatar": self.avatar,
        }
        response = self.client.post(reverse("valida_cadastro"), data)
        # Deve redirecionar após o cadastro
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("cadastro"))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Usuário já cadastrado!', messages)

    def test_valida_login_view_success(self):
        data = {
            "nome": self.user.username,
            "senha": self.user.password
        }
        response = self.client.post(reverse("valida_login"), data)
        # Deve redirecionar após o login
        self.assertEqual(response.status_code, 302)

    def test_valida_login_view_invalid_credentials(self):
        data = {"nome": "testuser", "senha": "wrongpassword"}
        response = self.client.post(reverse("valida_login"), data)
        # Deve redirecionar após a validação
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Usuario ou senha inválido!', messages)

    def test_sair_view(self):
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        response = self.client.get(reverse("sair"))
        # Deve redirecionar após o logout
        self.assertEqual(response.status_code, 302)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Faça login antes de acessar a plataforma!', messages)
