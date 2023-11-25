from django.test import TestCase
from ..models import Livros


class LivrosModelTestCase(TestCase):
    def setUp(self):
        Livros.objects.create(
            nome_livro="Livro 1",
            descricao="Descrição do Livro 1",
            n_paginas=200
        )

        Livros.objects.create(
            nome_livro="Livro 2",
            descricao="Descrição do Livro 2",
            n_paginas=300
        )

    def test_nome_livro(self):
        livro1 = Livros.objects.get(nome_livro="Livro 1")
        livro2 = Livros.objects.get(nome_livro="Livro 2")
        self.assertEqual(livro1.nome_livro, "Livro 1")
        self.assertEqual(livro2.nome_livro, "Livro 2")

    def test_descricao(self):
        livro1 = Livros.objects.get(nome_livro="Livro 1")
        livro2 = Livros.objects.get(nome_livro="Livro 2")
        self.assertEqual(livro1.descricao, "Descrição do Livro 1")
        self.assertEqual(livro2.descricao, "Descrição do Livro 2")

    def test_n_paginas(self):
        livro1 = Livros.objects.get(nome_livro="Livro 1")
        livro2 = Livros.objects.get(nome_livro="Livro 2")
        self.assertEqual(livro1.n_paginas, 200)
        self.assertEqual(livro2.n_paginas, 300)
