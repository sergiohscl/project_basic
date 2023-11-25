from django.http import HttpRequest
from django.test import TestCase
from ..forms import Livro


class LivroFormTestCase(TestCase):
    def setUp(self):
        self.form = Livro()

    def test_fields_form(self):
        self.assertIn('nome_livro', self.form.fields)
        self.assertIn('descricao', self.form.fields)
        self.assertIn('n_paginas', self.form.fields)

    def test_form_is_valid(self):
        request = HttpRequest()
        request.POST = {
            "nome_livro": "Python",
            "descricao": "Melhor linguagem de programação",
            "n_paginas": 210
        }
        form = Livro(request.POST)
        self.assertTrue(form.is_valid())
