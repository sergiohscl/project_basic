from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Livros

User = get_user_model()


class BaseTestCase(TestCase):
    def setUp(self):
        self.email = "samu@example.com"
        self.name = "samu"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.name, email=self.email, password=self.password
        )

        self.livro = Livros.objects.create(
            nome_livro='livro1',
            descricao='descricao livro1',
            n_paginas=200
        )

        self.client = APIClient(enforce_csrf_checks=True)
        self.client.force_authenticate(user=self.user)


class LivrosViewSetTestCase(BaseTestCase):
    def test_list_livros(self):
        # Testando a listagem de livros (GET)
        url = reverse('livros')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_livros_UNAUTHORIZED(self):
        self.client.force_authenticate(user=None)
        url = reverse('livros')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_livros(self):
        url = '/plataforma/livro/'
        data = {
            "nome_livro": self.livro.nome_livro,
            "descricao": self.livro.descricao,
            "n_paginas": self.livro.n_paginas
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_livro(self):
        url = f'/plataforma/livro/{self.livro.id}/'
        updated_data = {
            "nome_livro": "Livro 1 (Atualizado)",
            "descricao": "Nova descrição do Livro 1",
            "n_paginas": 250
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_livro(self):
        url = f'/plataforma/livro/{self.livro.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Livros.DoesNotExist):
            Livros.objects.get(pk=self.livro.id)
