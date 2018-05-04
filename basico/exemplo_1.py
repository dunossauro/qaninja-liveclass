"""caracteristicas gerais."""

a = 7
b = 'eduardo'


def func(x, y):
    return x + y


print(func(7, 7))


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa(nome="{self.nome}", idade={self.idade})'
