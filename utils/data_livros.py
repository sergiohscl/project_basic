from faker import Faker
import pymysql
from decouple import config

# Conectar ao banco de dados
db = pymysql.connect(
    host=config("DB_LOCALHOST"),
    user=config("DB_USER"),
    password=config("DB_PASSWORD"),
    database=config("DB_DATABASE"),
)
cursor = db.cursor()

# Inicializar o Faker
fake = Faker()


def insert_plataforma_livros(num_registros):
    for _ in range(num_registros):
        nome_livro = fake.sentence(nb_words=3),
        descricao = fake.paragraph(),
        n_paginas = fake.random_int(min=50, max=500),

        cursor.execute("INSERT INTO plataforma_livros (nome_livro, descricao, n_paginas) VALUES (%s, %s, %s)", (nome_livro, descricao, n_paginas))  # noqa E501
        db.commit()


# Inserir livros
insert_plataforma_livros(10)

# Fechar a conexão com o banco de dados
db.close()
